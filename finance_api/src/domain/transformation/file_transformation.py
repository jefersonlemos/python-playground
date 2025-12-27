import csv
import io
from typing import Dict, List, Any
from fastapi import UploadFile, HTTPException
import ofxparse


class FileTransformer:
    def __init__(self, profile: Dict[str, str] = None):
        # Default profile maps common fields
        self.profile = profile or {
            'date': 'Date',
            'amount': 'Amount',
            'memo': 'Description',
            'payee': 'Payee'
        }

    def transform(self, file: UploadFile) -> str:
        # Determine file type
        filename = file.filename.lower()
        if filename.endswith('.ofx'):
            return self._transform_ofx(file)
        elif filename.endswith('.csv'):
            return self._transform_csv(file)
        else:
            raise HTTPException(status_code=400, detail="Unsupported file type")

    def _transform_ofx(self, file: UploadFile) -> str:
        # Read file content
        content = file.file.read()
        file.file.seek(0)  # Reset file pointer
        ofx = ofxparse.OfxParser.parse(io.BytesIO(content))

        # Extract transactions
        transactions = []
        for account in ofx.accounts:
            for transaction in account.statement.transactions:
                transactions.append({
                    'date': transaction.date.strftime('%Y-%m-%d'),
                    'amount': str(transaction.amount),
                    'memo': transaction.memo or '',
                    'payee': transaction.payee or ''
                })

        return self._to_csv(transactions)

    def _transform_csv(self, file: UploadFile) -> str:
        # Assume CSV has headers: date,amount,memo,payee or similar
        content = file.file.read().decode('utf-8')
        file.file.seek(0)
        reader = csv.DictReader(io.StringIO(content))
        transactions = []
        for row in reader:
            transactions.append({
                'date': row.get('date', ''),
                'amount': row.get('amount', ''),
                'memo': row.get('memo', ''),
                'payee': row.get('payee', '')
            })

        return self._to_csv(transactions)

    def _to_csv(self, transactions: List[Dict[str, Any]]) -> str:
        if not transactions:
            return ''

        # Map using profile
        output_fields = list(self.profile.values())
        output = io.StringIO()
        writer = csv.DictWriter(output, fieldnames=output_fields)
        writer.writeheader()

        for tx in transactions:
            row = {}
            for input_field, output_field in self.profile.items():
                value = tx.get(input_field, '')
                # Sanitize
                value = self._sanitize_csv_value(value)
                row[output_field] = value
            writer.writerow(row)

        return output.getvalue()

    def _sanitize_csv_value(self, value: str) -> str:
        # Prefix dangerous cells with '
        dangerous_starts = ['=', '+', '-', '@']
        if any(value.startswith(start) for start in dangerous_starts):
            value = "'" + value
        return value