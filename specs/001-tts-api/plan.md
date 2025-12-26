# Implementation Plan: TTS API

**Branch**: `001-tts-api` | **Date**: 2025-12-25 | **Spec**: /home/relu/misc/local-voice-assistant-codex/specs/001-tts-api/spec.md
**Input**: Feature specification from `/specs/001-tts-api/spec.md`

## Summary

Build a FastAPI TTS service that accepts Japanese text, runs Style-Bert-VITS2,
returns WAV audio, supports basic voice/style selection, and provides structured
errors with a health endpoint.

## Technical Context

**Language/Version**: Python 3.11 (backend), Node.js 20 LTS (frontend), TypeScript 5.x  
**Primary Dependencies**: FastAPI, Pydantic, Uvicorn, uv, Ruff, Style-Bert-VITS2  
**Storage**: N/A (no persistence)  
**Testing**: pytest for API endpoints and error handling  
**Target Platform**: Local developer machines (macOS/Linux/Windows)  
**Project Type**: Web (backend + frontend)  
**Performance Goals**: 1-sentence request returns audio within 5 seconds  
**Constraints**: WAV output; no auth; no persistence  
**Scale/Scope**: Single service API for text → audio

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

- Decision: Use Style-Bert-VITS2 for Japanese TTS.  
  Rationale: Explicitly requested model.  
  Alternatives considered: Other TTS models.
- Decision: WAV output format.  
  Rationale: Most compatible and simple for TTS output.  
  Alternatives considered: MP3, WAV+MP3.
- Decision: 1,000 character max text length.  
  Rationale: Bounds compute and latency.  
  Alternatives considered: 2,000, 5,000.

## Phase 1: Design & Contracts

### Data Model

Documented in `/home/relu/misc/local-voice-assistant-codex/specs/001-tts-api/data-model.md`.

### API Contracts

OpenAPI contract for synthesis and health endpoints in
`/home/relu/misc/local-voice-assistant-codex/specs/001-tts-api/contracts/tts.openapi.yaml`.

### Quickstart

Developer setup and run steps captured in
`/home/relu/misc/local-voice-assistant-codex/specs/001-tts-api/quickstart.md`.

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
specs/001-tts-api/
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
│   │   └── tts.py
│   ├── services/
│   │   └── tts_engine.py
│   └── main.py
├── tests/
│   ├── test_health.py
│   └── test_tts.py
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
`frontend/` folders.

## Complexity Tracking

No constitution violations requiring justification.
