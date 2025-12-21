from datetime import datetime, timezone
from finance_api.utils.logging import LoggingOperations as logging
from fastapi import APIRouter, UploadFile, File
from pydantic import BaseModel

router = APIRouter(
    prefix="/import",
    tags=["file", "import"],
)

class ImportResponse(BaseModel):
    filename: str
    content_type: str | None
    status: str

@router.post(
    "",
    response_model=ImportResponse,
    summary="Import file",
    description="Receive a transaction file (OFX or CSV) and validate basic properties",
)

def import_file(file: UploadFile = File(...)) -> ImportResponse:
    if not file.filename:
        raise HTTPException(status_code=400, detail="File name is missing")

    filename = file.filename.lower()

    if not (filename.endswith(".ofx") or filename.endswith(".csv")):
        raise HTTPException(
            status_code=415,
            detail="Unsupported file type. Only .ofx and .csv are allowed",
        )

    return ImportResponse(
        filename=file.filename,
        content_type=file.content_type,
        status="received",
    )

