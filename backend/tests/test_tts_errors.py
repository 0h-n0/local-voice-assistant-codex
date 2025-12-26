from fastapi.testclient import TestClient

from app.main import app


def test_tts_empty_text_returns_error():
    client = TestClient(app)
    response = client.post("/tts/synthesize", json={"text": ""})
    assert response.status_code == 400
    payload = response.json()
    assert payload["code"] == "validation_error"
