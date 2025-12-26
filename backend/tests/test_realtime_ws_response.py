import json

from fastapi.testclient import TestClient

from app.api.realtime_ws import get_llm_client
from app.main import app
from app.services.llm_client import LlmResult


class FakeClient:
    def complete(self, prompt: str) -> LlmResult:
        return LlmResult(text="response", model="test")


def test_realtime_response_emits_audio():
    app.dependency_overrides[get_llm_client] = lambda: FakeClient()
    client = TestClient(app)
    with client.websocket_connect("/ws/voice") as websocket:
        websocket.send_bytes(b"frame")
        websocket.send_text(json.dumps({"event": "end"}))

        response_seen = False
        audio_event_seen = False
        audio_bytes_seen = False
        while True:
            message = websocket.receive()
            if message.get("text"):
                payload = json.loads(message["text"])
                if payload["type"] == "response":
                    response_seen = True
                if payload["type"] == "audio":
                    audio_event_seen = True
                if payload["type"] == "status" and payload["payload"]["state"] == "idle":
                    break
            if message.get("bytes"):
                audio_bytes_seen = True

        assert response_seen
        assert audio_event_seen
        assert audio_bytes_seen
    app.dependency_overrides.clear()
