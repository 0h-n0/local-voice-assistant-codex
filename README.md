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

## TTS API (WIP)

```bash
curl -X POST http://localhost:8000/tts/synthesize \
  -H "Content-Type: application/json" \
  -d '{"text": "こんにちは", "voice": "default"}' --output output.wav
```

## Orchestrator (WIP)

```bash
curl -F "file=@sample.wav" http://localhost:8000/orchestrate --output response.wav
```

## Conversation History API (WIP)

```bash
curl -X POST "http://localhost:8000/conversations/conv-001/messages" \
  -H "Content-Type: application/json" \
  -d '{"messages":[{"role":"user","content":"Hello"},{"role":"assistant","content":"Hi"}]}'
```

```bash
curl "http://localhost:8000/conversations/conv-001"
```

```bash
curl "http://localhost:8000/conversations"
```

```bash
curl -X DELETE "http://localhost:8000/conversations/conv-001"
```

## Voice Chat Web UI (WIP)

```bash
cd frontend
npm install
npm run dev
```

Open `http://localhost:3000` and use the recording controls to chat by voice.

## Realtime WebSocket (WIP)

Connect to `ws://localhost:8000/ws/voice` and stream WAV chunks (100–200ms). The
server emits `status`, `transcript`, `response`, and `audio` events.
