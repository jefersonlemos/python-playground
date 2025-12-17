from datetime import datetime, timezone

from fastapi import APIRouter
from pydantic import BaseModel

START_TIME = datetime.now(tz=timezone.utc)

router = APIRouter(
    prefix="/health",
    tags=["system"],
)


class HealthResponse(BaseModel):
    status: str
    uptime_seconds: float
    started_at: datetime


@router.get(
    "",
    response_model=HealthResponse,
    summary="Health check",
    description="Returns service health status and uptime.",
)
def health_check() -> HealthResponse:
    now = datetime.now(tz=timezone.utc)
    uptime = (now - START_TIME).total_seconds()

    return HealthResponse(
        status="ok",
        uptime_seconds=uptime,
        started_at=START_TIME,
    )
