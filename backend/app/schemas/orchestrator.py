from pydantic import BaseModel


class OrchestratorRequest(BaseModel):
    audio_bytes: bytes
