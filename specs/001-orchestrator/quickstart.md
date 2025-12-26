# Quickstart: Voice Orchestrator

**Date**: 2025-12-25
**Feature**: /home/relu/misc/local-voice-assistant-codex/specs/001-orchestrator/spec.md

## Prerequisites

- Python 3.11
- Node.js 20 LTS
- uv installed locally
- STT, LLM, and TTS services running locally

## Backend Setup

```bash
cd backend
uv sync
uv run uvicorn app.main:app --reload
```

## Orchestration Example

```bash
curl -F "file=@sample.wav" http://localhost:8000/orchestrate --output response.wav
```

Input and output are WAV only.

## Health Check

```bash
curl http://localhost:8000/health
```
