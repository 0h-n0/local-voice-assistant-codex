from dataclasses import dataclass


@dataclass(frozen=True)
class OrchestratorResult:
    stt_text: str
    llm_text: str
    audio_bytes: bytes


@dataclass(frozen=True)
class StageFailure(Exception):
    stage: str
    code: str
    message: str


class OrchestratorService:
    def run(self, audio_bytes: bytes) -> OrchestratorResult:
        if not audio_bytes:
            raise StageFailure(stage="stt", code="empty_audio", message="Audio input is required")
        stt_text = ""
        if not stt_text:
            raise StageFailure(
                stage="stt",
                code="empty_transcript",
                message="STT returned empty text",
            )
        llm_text = ""
        if not llm_text:
            raise StageFailure(
                stage="llm",
                code="empty_response",
                message="LLM returned empty response",
            )
        audio_bytes = b"RIFF"
        return OrchestratorResult(stt_text=stt_text, llm_text=llm_text, audio_bytes=audio_bytes)
