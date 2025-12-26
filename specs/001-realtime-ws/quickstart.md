# Quickstart: Realtime Voice WebSocket

## Connect and stream audio

1. Start backend:

```bash
cd backend
uv run --with uvicorn uvicorn app.main:app --reload
```

2. Connect with a WebSocket client (local):

```
ws://localhost:8000/ws/voice
```

3. Send audio frames (100–200ms WAV chunks) and receive events:

- `status` events for stream state
- `transcript` events for partial/final text
- `response` event for assistant text
- `audio` events with response audio frames
