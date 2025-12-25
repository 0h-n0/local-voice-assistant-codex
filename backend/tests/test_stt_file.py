from fastapi.testclient import TestClient

from app.main import app


def test_transcribe_file_returns_text():
    client = TestClient(app)
    response = client.post(
        "/stt/file",
        files={"file": ("sample.wav", b"RIFF", "audio/wav")},
        data={"audio_format": "wav"},
    )
    assert response.status_code == 200
    payload = response.json()
    assert "text" in payload
    assert payload["language"] == "ja"
