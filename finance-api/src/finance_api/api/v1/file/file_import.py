from datetime import datetime, timezone
from finance_api.utils.logging import LoggingOperations as logging
from fastapi import APIRouter, UploadFile, File
from pydantic import BaseModel

START_TIME = datetime.now(tz=timezone.utc)

router = APIRouter(
    prefix="/import",
    tags=["api, file, input"],
)


class ImportFile(BaseModel):
    file_name: str
    

@router.post(
    "",
    response_model=ImportFile,
    summary="Import file",
    description="Endpoint to receive files into the API",
)

def import_file(file: ImportFile) -> ImportFile:
    #TODO - This returns "file_name='transactions.ofx'", I need to get only the file name. 
    # Or not, need to check because I'm getting the full object only when printing, 
    # I'll have to test when using it to calculate something
    filezim = file
    logging(type="info", message="Started importing ${file}")

    return ImportFile(
        file_name=str(filezim)
    )