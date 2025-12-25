from fastapi.testclient import TestClient

from app.api.llm import get_llm_client
from app.main import app
from app.services.llm_client import LlmResult


class FakeClient:
    def complete(self, prompt: str) -> LlmResult:
        return LlmResult(text=f"echo:{prompt}", model="gpt-5-mini")


def test_llm_completion_returns_text():
    app.dependency_overrides[get_llm_client] = lambda: FakeClient()
    client = TestClient(app)
    response = client.post("/llm/complete", json={"prompt": "hello"})
    assert response.status_code == 200
    payload = response.json()
    assert payload["text"] == "echo:hello"
    assert payload["model"] == "gpt-5-mini"
    app.dependency_overrides.clear()


def test_llm_empty_prompt_returns_error():
    app.dependency_overrides[get_llm_client] = lambda: FakeClient()
    client = TestClient(app)
    response = client.post("/llm/complete", json={"prompt": ""})
    assert response.status_code == 400
    payload = response.json()
    assert payload["code"] == "validation_error"
    app.dependency_overrides.clear()
