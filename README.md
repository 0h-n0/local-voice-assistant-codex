# Local Voice Assistant

Monorepo for a local-first voice assistant.

## Projects

- `backend/`: FastAPI services
- `frontend/`: Next.js UI
- `specs/`: Feature specifications and plans

## STT API (WIP)

### File transcription

```bash
curl -F "file=@sample.wav" -F "audio_format=wav" http://localhost:8000/stt/file
```

### WebSocket streaming

Connect to `ws://localhost:8000/stt/stream`, send binary audio frames, then
send `{ "event": "end" }` to finalize.

### Health check

```bash
curl http://localhost:8000/health
```

## LLM Service (WIP)

### Prompt completion

```bash
curl -X POST http://localhost:8000/llm/complete \
  -H "Content-Type: application/json" \
  -d '{"prompt": "こんにちは"}'
```
