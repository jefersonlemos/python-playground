import pytest
from io import BytesIO
from fastapi import UploadFile
from domain.transformation.file_transformation import FileTransformer


@pytest.fixture
def sample_ofx_content():
    # Minimal OFX content for testing
    return b"""<?xml version="1.0" encoding="UTF-8"?>
<OFX>
    <BANKMSGSRSV1>
        <STMTTRNRS>
            <STMTRS>
                <BANKACCTFROM>
                    <BANKID>12345</BANKID>
                    <ACCTID>67890</ACCTID>
                    <ACCTTYPE>CHECKING</ACCTTYPE>
                </BANKACCTFROM>
                <BANKTRANLIST>
                    <DTSTART>20230101</DTSTART>
                    <DTEND>20230131</DTEND>
                    <STMTTRN>
                        <TRNTYPE>DEBIT</TRNTYPE>
                        <DTPOSTED>20230115</DTPOSTED>
                        <TRNAMT>-50.00</TRNAMT>
                        <MEMO>Test transaction</MEMO>
                        <PAYEE>Test Payee</PAYEE>
                    </STMTTRN>
                </BANKTRANLIST>
            </STMTRS>
        </STMTTRNRS>
    </BANKMSGSRSV1>
</OFX>"""


@pytest.fixture
def sample_csv_content():
    return "date,amount,memo,payee\n2023-01-15,-50.00,Test transaction,Test Payee\n"


@pytest.fixture
def transformer():
    return FileTransformer()


def test_transform_ofx(transformer, sample_ofx_content):
    file = UploadFile(filename="test.ofx", file=BytesIO(sample_ofx_content))
    result = transformer.transform(file)
    assert "Date,Amount,Description,Payee" in result
    assert "2023-01-15" in result
    assert "-50.00" in result


def test_transform_csv(transformer, sample_csv_content):
    file = UploadFile(filename="test.csv", file=BytesIO(sample_csv_content.encode()))
    result = transformer.transform(file)
    assert "Date,Amount,Description,Payee" in result
    assert "2023-01-15" in result
    assert "-50.00" in result


def test_sanitize_csv_value():
    transformer = FileTransformer()
    assert transformer._sanitize_csv_value("=formula") == "'=formula"
    assert transformer._sanitize_csv_value("+positive") == "'+positive"
    assert transformer._sanitize_csv_value("-negative") == "'-negative"
    assert transformer._sanitize_csv_value("@at") == "'@at"
    assert transformer._sanitize_csv_value("normal") == "normal"


def test_unsupported_file_type(transformer):
    file = UploadFile(filename="test.txt", file=BytesIO(b"content"))
    with pytest.raises(Exception):  # HTTPException
        transformer.transform(file)