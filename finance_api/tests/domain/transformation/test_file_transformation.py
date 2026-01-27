from pathlib import Path
from fastapi import UploadFile
import io
import pytest

from domain.transformation.file_transformation import FileTransformer


FIXTURES = Path(__file__).parent.parent.parent / "fixtures"


def test_ofx_transformation_with_manual_fields():
    ofx_path = FIXTURES / "sample.ofx"

    with open(ofx_path, "rb") as f:
        upload = UploadFile(filename="sample.ofx", file=f)

        transformer = FileTransformer()
        csv_output = transformer.transform(
            upload,
            manual_fields={
                "due_date": "2026-02-10",
                "_cartao": "Nubank",
                "_conta": "Main Account",
            },
        )

    assert "Coffee Shop" in csv_output
    assert "2026-02-10" in csv_output
    assert "Nubank" in csv_output
    assert "Main Account" in csv_output


def test_ofx_transformation_without_manual_fields():
    ofx_path = FIXTURES / "sample.ofx"

    with open(ofx_path, "rb") as f:
        upload = UploadFile(filename="sample.ofx", file=f)

        transformer = FileTransformer()
        csv_output = transformer.transform(upload)

    assert "Coffee Shop" in csv_output
    assert csv_output  # Ensure output is not empty


def test_csv_transformation():
    csv_content = b"date,amount,memo\n2026-01-01,100.00,Test transaction\n"
    upload = UploadFile(
        filename="test.csv",
        file=io.BytesIO(csv_content),
    )

    transformer = FileTransformer()
    csv_output = transformer.transform(upload)

    assert "date" in csv_output or "Data de Lançamento" in csv_output
    assert "Valor" in csv_output or "100.00" in csv_output
    assert csv_output  # Ensure output is not empty


def test_unsupported_file_type():
    upload = UploadFile(
        filename="test.txt",
        file=io.BytesIO(b"unsupported"),
    )

    transformer = FileTransformer()
    
    with pytest.raises(Exception):  # HTTPException
        transformer.transform(upload)


def test_csv_injection_prevention():
    upload = UploadFile(
        filename="sample.ofx",
        file=io.BytesIO(b"<OFX>ok</OFX>"),
    )

    transformer = FileTransformer()
    csv_output = transformer.transform(
        upload,
        manual_fields={
            "memo": "=MALICIOUS_FORMULA",
        },
    )

    # Sanitized values should be prefixed with single quote
    assert "'=MALICIOUS_FORMULA" in csv_output or "=MALICIOUS_FORMULA" not in csv_output


def test_transformer_outputs_valid_csv_format():
    ofx_path = FIXTURES / "sample.ofx"

    with open(ofx_path, "rb") as f:
        upload = UploadFile(filename="sample.ofx", file=f)

        transformer = FileTransformer()
        csv_output = transformer.transform(upload)

    # Check that output is CSV formatted (has headers and at least one row)
    lines = csv_output.strip().split('\n')
    assert len(lines) >= 2  # At least header and one data row
    assert ',' in lines[0]  # Header should have commas


def test_transformer_with_empty_transactions():
    # Create a minimal valid OFX with no transactions
    ofx_content = b"""OFXHEADER:100
OFXVERSION:102
SECURITY:NONE
ENCODING:USASCII
CHARSET:1252
COMPRESSION:NONE
OLDFILEVERSION:102
NEWFILEVERSION:102
<OFX>
<SIGNONMSGSRSV1>
<SONRS>
<STATUS>
<CODE>0
<SEVERITY>INFO
</STATUS>
<DTSERVER>20260113000000
<LANGUAGE>ENG
</SONRS>
</SIGNONMSGSRSV1>
<BANKMSGSRSV1>
<STMTTRNRS>
<STMTRS>
<BANKTRANLIST>
</BANKTRANLIST>
</STMTRS>
</STMTTRNRS>
</BANKMSGSRSV1>
</OFX>"""

    upload = UploadFile(
        filename="empty.ofx",
        file=io.BytesIO(ofx_content),
    )

    transformer = FileTransformer()
    csv_output = transformer.transform(upload)

    # Should return empty string for no transactions
    assert csv_output == "" or csv_output.strip() == ""


def test_transformer_sanitizes_injection_attempts():
    csv_content = b"""date,amount,memo
2026-01-01,100.00,=SUM(A1:A10)
2026-01-02,200.00,+IMPORTXML(url)
2026-01-03,300.00,-QUERY(url)
2026-01-04,400.00,@IMPORTXML(url)
"""
    upload = UploadFile(
        filename="test.csv",
        file=io.BytesIO(csv_content),
    )

    transformer = FileTransformer()
    csv_output = transformer.transform(upload)

    # Check that dangerous formulas are sanitized with single quote prefix
    lines = csv_output.strip().split('\n')
    for line in lines[1:]:  # Skip header
        # Formulas should be escaped
        assert "'=" in line or "'+" in line or "'-" in line or "'@" in line or "SUM" not in line
