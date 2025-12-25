from fastapi import APIRouter
from pydantic import BaseModel

router = APIRouter()


class HealthStatus(BaseModel):
    status: str


@router.get("/health", response_model=HealthStatus)
def health_check() -> HealthStatus:
    return HealthStatus(status="ok")
