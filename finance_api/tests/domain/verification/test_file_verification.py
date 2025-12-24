import io
import pytest
from fastapi import UploadFile
from domain.verification.file_verification import verify_uploaded_file

def make_upload_file(filename: str, content: bytes) -> UploadFile:
    return UploadFile(
        filename=filename,
        file=io.BytesIO(content),
    )

# -------------------------
# VALID FILES
# -------------------------

def test_valid_ofx_file():
    file = make_upload_file(
        "test.ofx",
        b"<OFX>\n<SIGNONMSGSRSV1>",
    )

    # should NOT raise
    verify_uploaded_file(file)


def test_valid_csv_file_with_comma():
    file = make_upload_file(
        "test.csv",
        b"col1,col2,col3\n1,2,3",
    )

    verify_uploaded_file(file)


def test_valid_csv_file_with_semicolon():
    file = make_upload_file(
        "test.csv",
        b"col1;col2;col3\n1;2;3",
    )

    verify_uploaded_file(file)


# -------------------------
# FAILURE CASES
# -------------------------

def test_empty_file():
    file = make_upload_file("empty.csv", b"")

    with pytest.raises(ValueError, match="Empty file"):
        verify_uploaded_file(file)


def test_binary_file_rejected():
    file = make_upload_file(
        "binary.csv",
        b"\x00\x01\x02\x03",
    )

    with pytest.raises(ValueError, match="Binary content detected"):
        verify_uploaded_file(file)


def test_invalid_utf8_file():
    file = make_upload_file(
        "invalid.csv",
        b"\xff\xfe\xfd",
    )

    with pytest.raises(ValueError, match="File is not valid UTF-8 text"):
        verify_uploaded_file(file)


def test_invalid_ofx_header():
    file = make_upload_file(
        "bad.ofx",
        b"THIS IS NOT OFX",
    )

    with pytest.raises(ValueError, match="Invalid OFX header"):
        verify_uploaded_file(file)


def test_invalid_csv_structure():
    file = make_upload_file(
        "bad.csv",
        b"this has no delimiters at all",
    )

    with pytest.raises(ValueError, match="Invalid CSV structure"):
        verify_uploaded_file(file)


def test_unsupported_extension():
    file = make_upload_file(
        "file.txt",
        b"just some text",
    )

    with pytest.raises(ValueError, match="Unsupported file extension"):
        verify_uploaded_file(file)
