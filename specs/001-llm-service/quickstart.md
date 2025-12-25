# Quickstart: LLM Service

**Date**: 2025-12-25
**Feature**: /home/relu/misc/local-voice-assistant-codex/specs/001-llm-service/spec.md

## Prerequisites

- Python 3.11
- Node.js 20 LTS
- uv installed locally
- OpenAI API key available

## Backend Setup

```bash
cd backend
uv sync
export OPENAI_API_KEY=your-key
uv run uvicorn app.main:app --reload
```

## Completion Example

```bash
curl -X POST http://localhost:8000/llm/complete \
  -H "Content-Type: application/json" \
  -d '{"prompt": "こんにちは"}'
```

Prompt length is limited to 4,000 characters.

## Health Check

```bash
curl http://localhost:8000/health
```
