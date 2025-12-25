from fastapi import FastAPI

from app.api.health import router as health_router
from app.api.stt import router as stt_router

app = FastAPI()
app.include_router(health_router)
app.include_router(stt_router)
