from fastapi import APIRouter
from api.v1.health import router as health_router
from api.v1.file import router as file_router

router = APIRouter(prefix="/v1")

router.include_router(health_router)
router.include_router(file_router)
