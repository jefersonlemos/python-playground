import csv
import io
from typing import Dict, List, Any
from fastapi import UploadFile, HTTPException
from domain.transformation.profiles import *
import ofxparse


class FileTransformer:
    def __init__(self, profile: dict = DEFAULT_PROFILE):
        self.profile = profile

    def transform(self, file: UploadFile) -> str:
        filename = file.filename.lower()

        if filename.endswith(".ofx"):
            return self._transform_ofx(file)
        elif filename.endswith(".csv"):
            return self._transform_csv(file)

        raise HTTPException(status_code=400, detail="Unsupported file type")

    def _transform_ofx(self, file: UploadFile) -> str:
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
                    "payee": transaction.payee or "",
                })

        return self._to_csv(transactions)

    def _transform_csv(self, file: UploadFile) -> str:
        content = file.file.read().decode("utf-8")
        file.file.seek(0)

        reader = csv.DictReader(io.StringIO(content))
        transactions = []

        for row in reader:
            transactions.append({
                "date": row.get("date", ""),
                "amount": row.get("amount", ""),
                "memo": row.get("memo", ""),
                "payee": row.get("payee", ""),
            })

        return self._to_csv(transactions)

    def _to_csv(self, transactions: List[Dict[str, Any]]) -> str:
        if not transactions:
            return ""

        output_fields = [cfg["column"] for cfg in self.profile.values()]
        output = io.StringIO()

        writer = csv.DictWriter(output, fieldnames=output_fields)
        writer.writeheader()

        for tx in transactions:
            row = {}

            for input_field, cfg in self.profile.items():
                value = tx.get(input_field)

                if not value:
                    value = cfg["default"]

                value = self._sanitize_csv_value(str(value))
                row[cfg["column"]] = value

            writer.writerow(row)

        return output.getvalue()

    def _sanitize_csv_value(self, value: str) -> str:
        dangerous_starts = ("=", "+", "-", "@")
        if value.startswith(dangerous_starts):
            return "'" + value
        return value