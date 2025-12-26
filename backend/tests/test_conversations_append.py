from fastapi.testclient import TestClient

from app.api.conversations import get_conversation_store
from app.main import app
from app.services.conversation_store import ConversationStore


def test_append_messages_creates_conversation(tmp_path):
    store = ConversationStore(str(tmp_path / "conversations.db"))
    app.dependency_overrides[get_conversation_store] = lambda: store
    client = TestClient(app)

    response = client.post(
        "/conversations/conv-1/messages",
        json={"messages": [{"role": "user", "content": "Hello"}]},
    )

    assert response.status_code == 200
    payload = response.json()
    assert payload["id"] == "conv-1"
    assert len(payload["messages"]) == 1
    assert payload["messages"][0]["role"] == "user"
    app.dependency_overrides.clear()
