from fastapi import APIRouter
from finance_api.api.v1.file.file_import import router as import_router


router = APIRouter(prefix="/file")
router.include_router(import_router)
