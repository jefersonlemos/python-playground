import csv
import io
from typing import Dict, List, Any
from fastapi import UploadFile, HTTPException
import ofxparse

from domain.transformation.profiles import DEFAULT_PROFILE


class FileTransformer:
    def __init__(self, profile: dict = DEFAULT_PROFILE):
        self.profile = profile

    def transform(
        self,
        file: UploadFile,
        manual_fields: Dict[str, Any] | None = None,
    ) -> str:
        filename = file.filename.lower()
        manual_fields = manual_fields or {}

        if filename.endswith(".ofx"):
            transactions = self._parse_ofx(file)
        elif filename.endswith(".csv"):
            transactions = self._parse_csv(file)
        else:
            raise HTTPException(status_code=400, detail="Unsupported file type")

        return self._to_csv(transactions, manual_fields)

    def _parse_ofx(self, file: UploadFile) -> List[Dict[str, Any]]:
        content = file.file.read()
        file.file.seek(0)

        ofx = ofxparse.OfxParser.parse(io.BytesIO(content))

        transactions = []
        for account in ofx.accounts:
            for transaction in account.statement.transactions:
                transactions.append({
                    "date": transaction.date.strftime("%Y-%m-%d"),
                    "amount": str(transaction.amount),
                    "memo": transaction.memo or "",
                })

        return transactions

    def _parse_csv(self, file: UploadFile) -> List[Dict[str, Any]]:
        content = file.file.read().decode("utf-8")
        file.file.seek(0)

        reader = csv.DictReader(io.StringIO(content))
        return list(reader)

    def _to_csv(
        self,
        transactions: List[Dict[str, Any]],
        manual_fields: Dict[str, Any],
    ) -> str:
        if not transactions:
            return ""

        output_fields = [cfg["column"] for cfg in self.profile.values()]
        output = io.StringIO()

        writer = csv.DictWriter(output, fieldnames=output_fields)
        writer.writeheader()

        for tx in transactions:
            row = {}

            for input_field, cfg in self.profile.items():
                value = (
                    tx.get(input_field)
                    or manual_fields.get(input_field)
                    or cfg["default"]
                )

                value = self._sanitize_csv_value(str(value))
                row[cfg["column"]] = value

            writer.writerow(row)

        return output.getvalue()

    def _sanitize_csv_value(self, value: str) -> str:
        # Prevent CSV injection
        if value.startswith(("=", "+", "-", "@")):
            return "'" + value
        return value
