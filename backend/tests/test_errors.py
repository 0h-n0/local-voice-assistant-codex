from fastapi.testclient import TestClient

from app.main import app


def test_unsupported_audio_format_returns_error():
    client = TestClient(app)
    response = client.post(
        "/stt/file",
        files={"file": ("sample.wav", b"RIFF", "audio/wav")},
        data={"audio_format": "aac"},
    )
    assert response.status_code == 400
    payload = response.json()
    assert payload["code"] == "unsupported_audio_format"
