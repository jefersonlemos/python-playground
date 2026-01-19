from fastapi import APIRouter, UploadFile, File, HTTPException, Form
from pydantic import BaseModel

from utils.logging import LoggingOperations as logging
from domain.verification.file_verification import verify_uploaded_file
from domain.verification.file_verification import enforce_size
from domain.transformation.file_transformation import FileTransformer


router = APIRouter(
    prefix="/import",
    tags=["file", "import"],
)

class ImportResponse(BaseModel):
    filename: str
    content_type: str | None
    csv_content: str

@router.post(
    "",
    response_model=ImportResponse,
    summary="Import and transform file",
    description="Receive a transaction file (OFX or CSV), validate it, and return a transformed CSV",
)
async def import_file(
    file: UploadFile = File(...),
    due_date: str | None = Form(None),
    card_name: str | None = Form(None),
    account: str | None = Form(None),
) -> ImportResponse:

    if not file.filename:
        logging("error", "File upload without filename")
        raise HTTPException(status_code=400, detail="File name is missing")

    await enforce_size(file)
    try:
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

    transformer = FileTransformer()

    csv_content = transformer.transform(
        file,
        manual_fields={
            "due_date": due_date,
            "_cartao": card_name,
            "_conta": account,
        },
    )

    return ImportResponse(
        filename=file.filename,
        content_type=file.content_type,
        csv_content=csv_content,
    )
