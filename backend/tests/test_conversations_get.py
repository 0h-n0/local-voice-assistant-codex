from fastapi.testclient import TestClient

from app.api.conversations import get_conversation_store
from app.main import app
from app.services.conversation_store import ConversationStore


def test_get_conversation_returns_messages_in_order(tmp_path):
    store = ConversationStore(str(tmp_path / "conversations.db"))
    app.dependency_overrides[get_conversation_store] = lambda: store
    client = TestClient(app)

    client.post(
        "/conversations/conv-1/messages",
        json={
            "messages": [
                {"role": "user", "content": "Hi"},
                {"role": "assistant", "content": "Hello"},
            ]
        },
    )

    response = client.get("/conversations/conv-1")
    assert response.status_code == 200
    payload = response.json()
    assert payload["id"] == "conv-1"
    assert [msg["role"] for msg in payload["messages"]] == ["user", "assistant"]
    app.dependency_overrides.clear()
