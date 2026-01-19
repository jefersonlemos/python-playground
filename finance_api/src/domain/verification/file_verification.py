from fastapi import UploadFile, HTTPException

MAX_SIZE = 2 * 1024 * 1024  #2 MB

async def enforce_size(file: UploadFile):
    size = 0
    chunk_size = 1024 * 1024

    while chunk := await file.read(chunk_size):
        size += len(chunk)
        if size > MAX_SIZE:
            raise ValueError("File too large")
    await file.seek(0)

def verify_uploaded_file(file: UploadFile, sniff_bytes: int = 4096) -> None:
    """
    Verifies the uploaded file using cheap, defensive checks.
    - Reads only the first N bytes
    - Rejects binary blobs
    - Performs minimal format sniffing (CSV / OFX)
    Raises ValueError on failure.
    """

    head = file.file.read(sniff_bytes)
    file.file.seek(0)

    if not head:
        raise ValueError("Empty file")

    # Reject null bytes (binary check)
    if b"\x00" in head:
        raise ValueError("Binary content detected")

    # Try text decoding
    try:
        text = head.decode("utf-8", errors="strict")
    except UnicodeDecodeError:
        raise ValueError("File is not valid UTF-8 text")

    lower_name = file.filename.lower()

    if lower_name.endswith(".ofx"):
        if "<ofx" not in text.lower():
            raise ValueError("Invalid OFX header")

    elif lower_name.endswith(".csv"):
        if "," not in text and ";" not in text:
            raise ValueError("Invalid CSV structure")

    else:
        raise ValueError("Unsupported file extension")