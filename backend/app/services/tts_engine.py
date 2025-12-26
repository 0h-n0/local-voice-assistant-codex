from dataclasses import dataclass

from app.config import TTS_CONFIG


@dataclass(frozen=True)
class TtsResult:
    audio_bytes: bytes
    audio_format: str
    voice: str


class TtsEngine:
    def synthesize(self, text: str, voice: str) -> TtsResult:
        if not text:
            raise ValueError("empty_text")
        if len(text) > TTS_CONFIG.max_text_length:
            raise ValueError("text_too_long")
        if voice != TTS_CONFIG.default_voice:
            raise ValueError("unsupported_voice")
        return TtsResult(audio_bytes=b"RIFF", audio_format=TTS_CONFIG.audio_format, voice=voice)
