# WebSocket Streaming Contract: STT API

**Endpoint**: `/stt/stream`

## Client → Server

- Open WebSocket connection
- Send binary audio frames (WAV/FLAC/MP3) sized <= 1 second each
- Send JSON control message `{ "event": "end" }` to finalize

## Server → Client

- On partial transcription: `{ "event": "partial", "text": "..." }`
- On final transcription: `{ "event": "final", "text": "..." }`
- On error: `{ "event": "error", "code": "...", "message": "..." }`
