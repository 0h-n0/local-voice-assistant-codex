# Implementation Plan: STT API

**Branch**: `001-stt-api` | **Date**: 2025-12-25 | **Spec**: /home/relu/misc/local-voice-assistant-codex/specs/001-stt-api/spec.md
**Input**: Feature specification from `/specs/001-stt-api/spec.md`

## Summary

Deliver a FastAPI-based STT service that accepts Japanese audio file uploads and
WebSocket microphone streams, returning plain text transcriptions and structured
errors, with health checks and documented usage.

## Technical Context

**Language/Version**: Python 3.11 (backend), Node.js 20 LTS (frontend), TypeScript 5.x  
**Primary Dependencies**: FastAPI, Pydantic, Uvicorn, uv, Ruff, reazon-research/reazonspeech-nemo-v2  
**Storage**: N/A (no persistence required)  
**Testing**: pytest for API endpoints and WebSocket streaming  
**Target Platform**: Local developer machines (macOS/Linux/Windows)  
**Project Type**: Web (backend + frontend)  
**Performance Goals**: Transcription for 10-second audio returns within 10 seconds  
**Constraints**: Offline-first; no authentication; no external services  
**Scale/Scope**: Single service API with file + streaming inputs

## Constitution Check

*GATE: Must pass before Phase 0 research. Re-check after Phase 1 design.*

- [x] Local-first privacy honored (no network or telemetry without explicit approval)
- [x] Scriptable interfaces with stable input/output contracts
- [x] Critical-path tests planned for routing, parsing, persistence, or device control
- [x] Observability plan includes structured logs and opt-in diagnostics
- [x] Versioning and migration impact documented for any contract changes
- [x] Tooling compliance: uv for Python dependencies, Ruff linting, Pydantic validation
- [x] Stack compliance: React/Next (TypeScript) frontend and FastAPI backend
- [x] Workflow compliance: branch before work, README updated, PR ready for review

## Phase 0: Research

### Findings

- Decision: Use reazon-research/reazonspeech-nemo-v2 for Japanese STT.  
  Rationale: Explicitly requested model with Japanese support.  
  Alternatives considered: Whisper, NeMo ASR baselines.
- Decision: WebSocket streaming for microphone input.  
  Rationale: Low-latency streaming matches live transcription use cases.  
  Alternatives considered: Chunked HTTP uploads.
- Decision: WAV/FLAC/MP3 upload support.  
  Rationale: Common audio formats with broad tooling support.  
  Alternatives considered: WAV-only.
- Decision: 60-second maximum audio length per request.  
  Rationale: Bounds compute for local use and keeps latency predictable.  
  Alternatives considered: 30s, 300s.

## Phase 1: Design & Contracts

### Data Model

Documented in `/home/relu/misc/local-voice-assistant-codex/specs/001-stt-api/data-model.md`.

### API Contracts

OpenAPI contract for file transcription and health endpoints in
`/home/relu/misc/local-voice-assistant-codex/specs/001-stt-api/contracts/stt.openapi.yaml`.
WebSocket streaming contract documented in
`/home/relu/misc/local-voice-assistant-codex/specs/001-stt-api/contracts/stt.websocket.md`.

### Quickstart

Developer setup and run steps captured in
`/home/relu/misc/local-voice-assistant-codex/specs/001-stt-api/quickstart.md`.

### Post-Design Constitution Check

- [x] Local-first privacy honored (no network or telemetry without explicit approval)
- [x] Scriptable interfaces with stable input/output contracts
- [x] Critical-path tests planned for routing, parsing, persistence, or device control
- [x] Observability plan includes structured logs and opt-in diagnostics
- [x] Versioning and migration impact documented for any contract changes
- [x] Tooling compliance: uv for Python dependencies, Ruff linting, Pydantic validation
- [x] Stack compliance: React/Next (TypeScript) frontend and FastAPI backend
- [x] Workflow compliance: branch before work, README updated, PR ready for review

## Project Structure

### Documentation (this feature)

```text
specs/001-stt-api/
├── plan.md              # This file (/speckit.plan command output)
├── research.md          # Phase 0 output (/speckit.plan command)
├── data-model.md        # Phase 1 output (/speckit.plan command)
├── quickstart.md        # Phase 1 output (/speckit.plan command)
├── contracts/           # Phase 1 output (/speckit.plan command)
└── tasks.md             # Phase 2 output (/speckit.tasks command - NOT created by /speckit.plan)
```

### Source Code (repository root)

```text
backend/
├── app/
│   ├── api/
│   │   ├── health.py
│   │   └── stt.py
│   ├── services/
│   │   └── transcription.py
│   └── main.py
├── tests/
│   ├── test_health.py
│   └── test_stt.py
├── pyproject.toml
└── uv.lock

frontend/
├── app/
│   └── page.tsx
├── public/
├── package.json
├── tsconfig.json
└── next.config.js

README.md
```

**Structure Decision**: Reuse the existing monorepo layout with `backend/` and
`frontend/` folders to align with the scaffold.

## Complexity Tracking

No constitution violations requiring justification.
