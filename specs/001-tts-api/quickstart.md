# Quickstart: TTS API

**Date**: 2025-12-25
**Feature**: /home/relu/misc/local-voice-assistant-codex/specs/001-tts-api/spec.md

## Prerequisites

- Python 3.11
- Node.js 20 LTS
- uv installed locally
- Style-Bert-VITS2 model assets available locally

## Backend Setup

```bash
cd backend
uv sync
uv run uvicorn app.main:app --reload
```

## Synthesis Example

```bash
curl -X POST http://localhost:8000/tts/synthesize \
  -H "Content-Type: application/json" \
  -d '{"text": "こんにちは", "voice": "default"}' --output output.wav
```

Text length is limited to 1,000 characters.

## Health Check

```bash
curl http://localhost:8000/health
```
