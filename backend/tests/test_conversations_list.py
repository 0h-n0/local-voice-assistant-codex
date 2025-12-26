from fastapi.testclient import TestClient

from app.api.conversations import get_conversation_store
from app.main import app
from app.services.conversation_store import ConversationStore


def test_list_conversations_returns_summaries(tmp_path):
    store = ConversationStore(str(tmp_path / "conversations.db"))
    app.dependency_overrides[get_conversation_store] = lambda: store
    client = TestClient(app)

    client.post(
        "/conversations/conv-1/messages",
        json={"messages": [{"role": "user", "content": "First"}]},
    )
    client.post(
        "/conversations/conv-2/messages",
        json={"messages": [{"role": "user", "content": "Second"}]},
    )

    response = client.get("/conversations")
    assert response.status_code == 200
    payload = response.json()
    ids = {item["id"] for item in payload["conversations"]}
    assert ids == {"conv-1", "conv-2"}
    app.dependency_overrides.clear()
