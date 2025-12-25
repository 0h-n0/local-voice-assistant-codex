from fastapi.testclient import TestClient

from app.api.llm import get_llm_client
from app.main import app
from app.services.llm_client import LlmProviderError


class FailingClient:
    def complete(self, prompt: str):
        raise LlmProviderError("provider_error", "Upstream provider error")


def test_llm_provider_error_returns_structured_response():
    app.dependency_overrides[get_llm_client] = lambda: FailingClient()
    client = TestClient(app)
    response = client.post("/llm/complete", json={"prompt": "hello"})
    assert response.status_code == 502
    payload = response.json()
    assert payload["code"] == "provider_error"
    app.dependency_overrides.clear()
