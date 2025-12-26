import os
from dataclasses import dataclass

from openai import OpenAI

from app.config import LLM_CONFIG, SETTINGS


@dataclass(frozen=True)
class LlmResult:
    text: str
    model: str


class LlmProviderError(RuntimeError):
    def __init__(self, code: str, message: str) -> None:
        super().__init__(message)
        self.code = code
        self.message = message


class LlmClient:
    def __init__(self, api_key: str | None = None) -> None:
        self._api_key = api_key or SETTINGS.openai_api_key or os.getenv("OPENAI_API_KEY")
        if not self._api_key:
            raise LlmProviderError("missing_api_key", "Missing OpenAI API key")
        self._client = OpenAI(api_key=self._api_key)

    def complete(self, prompt: str) -> LlmResult:
        try:
            response = self._client.responses.create(
                model=LLM_CONFIG.model,
                input=prompt,
            )
        except Exception as exc:
            raise LlmProviderError("provider_error", "Upstream provider error") from exc
        text = getattr(response, "output_text", "")
        return LlmResult(text=text, model=LLM_CONFIG.model)
