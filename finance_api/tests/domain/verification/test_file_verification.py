import io
import pytest
from fastapi import UploadFile

from domain.verification.file_verification import verify_uploaded_file


def make_upload(filename: str, content: bytes):
    return UploadFile(
        filename=filename,
        file=io.BytesIO(content),
    )


def test_valid_ofx_file():
    file = make_upload("test.ofx", b"<OFX>ok</OFX>")
    verify_uploaded_file(file)


def test_rejects_binary_file():
    file = make_upload("bad.ofx", b"\x00\x01\x02")
    with pytest.raises(ValueError):
        verify_uploaded_file(file)


def test_rejects_unsupported_extension():
    file = make_upload("file.exe", b"text")
    with pytest.raises(ValueError):
        verify_uploaded_file(file)
