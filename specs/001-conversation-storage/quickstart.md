# Quickstart: Conversation History Storage

## Append messages to a conversation

```bash
curl -X POST "http://localhost:8000/conversations/conv-001/messages" \
  -H "Content-Type: application/json" \
  -d '{
    "messages": [
      {"role": "user", "content": "Hello"},
      {"role": "assistant", "content": "Hi there"}
    ]
  }'
```

## Retrieve a conversation

```bash
curl "http://localhost:8000/conversations/conv-001"
```

## List conversations

```bash
curl "http://localhost:8000/conversations"
```

## Delete a conversation

```bash
curl -X DELETE "http://localhost:8000/conversations/conv-001"
```
