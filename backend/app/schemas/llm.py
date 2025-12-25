from pydantic import BaseModel, Field

from app.config import LLM_CONFIG


class LlmRequest(BaseModel):
    prompt: str = Field(min_length=1, max_length=LLM_CONFIG.max_prompt_length)


class LlmResponse(BaseModel):
    request_id: str
    text: str
    model: str
