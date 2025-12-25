# Quickstart: STT API

**Date**: 2025-12-25
**Feature**: /home/relu/misc/local-voice-assistant-codex/specs/001-stt-api/spec.md

## Prerequisites

- Python 3.11
- Node.js 20 LTS
- uv installed locally

## Backend Setup

```bash
cd backend
uv sync
uv run uvicorn app.main:app --reload
```

## File Transcription Example

```bash
curl -F "file=@sample.wav" -F "audio_format=wav" http://localhost:8000/stt/file
```

## WebSocket Streaming Example

Use a WebSocket client to connect to `ws://localhost:8000/stt/stream`, send
binary frames, and finish with `{ "event": "end" }`.

## Health Check

```bash
curl http://localhost:8000/health
```
