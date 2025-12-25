from dataclasses import dataclass
from typing import BinaryIO

from app.config import DEFAULT_CONFIG
from app.services.model_loader import ModelLoader


@dataclass(frozen=True)
class TranscriptionOutput:
    text: str
    language: str
    confidence: float


class TranscriptionService:
    def __init__(self) -> None:
        self._model = ModelLoader().load()

    def transcribe_file(self, stream: BinaryIO, audio_format: str) -> TranscriptionOutput:
        if audio_format not in DEFAULT_CONFIG.supported_formats:
            raise ValueError("unsupported_audio_format")
        return TranscriptionOutput(text="", language="ja", confidence=0.0)

    def transcribe_stream(self, frames: list[bytes]) -> TranscriptionOutput:
        if not frames:
            raise ValueError("empty_stream")
        return TranscriptionOutput(text="", language="ja", confidence=0.0)
