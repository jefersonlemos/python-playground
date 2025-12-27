from datetime import datetime, timezone
from utils.logging import LoggingOperations as logging
from domain.verification.file_verification import enforce_size, verify_uploaded_file
from domain.transformation.file_transformation import FileTransformer
from fastapi import APIRouter, UploadFile, File, HTTPException
from pydantic import BaseModel

router = APIRouter(
    prefix="/import",
    tags=["file", "import"],
)

class ImportResponse(BaseModel):
    filename: str
    content_type: str | None
    status: str
    csv_content: str

@router.post(
    "",
    response_model=ImportResponse,
    summary="Import file",
    description="Receive a transaction file (OFX or CSV) and validate basic properties",
)

async def import_file(file: UploadFile = File(...)) -> ImportResponse:
    if not file.filename:
        logging("error", "File upload without filename")
        raise HTTPException(status_code=400, detail="File name is missing")

    try:
        await enforce_size(file)
        verify_uploaded_file(file)
    except ValueError as exc:
        logging("warning", f"File verification failed: {exc}")
        raise HTTPException(status_code=422, detail=str(exc))
    except Exception as exc:
        logging("error", f"Unexpected verification error: {exc}")
        raise HTTPException(status_code=500, detail="Internal verification error")


    logging(
        "info",
        f"File verified successfully: {file.filename} ({file.content_type})",
    )

    # Transform the file
    transformer = FileTransformer()
    csv_content = transformer.transform(file)

    logging(
        "info",
        f"File transformed successfully",
    )

    return ImportResponse(
        filename=file.filename,
        content_type=file.content_type,
        status="transformed",
        csv_content=csv_content,
    )
