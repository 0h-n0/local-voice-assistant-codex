# Implementation Plan: Voice Orchestrator

**Branch**: `001-orchestrator` | **Date**: 2025-12-25 | **Spec**: /home/relu/misc/local-voice-assistant-codex/specs/001-orchestrator/spec.md
**Input**: Feature specification from `/specs/001-orchestrator/spec.md`

## Summary

Create a FastAPI orchestrator that runs STT → LLM → TTS sequentially, accepts WAV
input, returns WAV output, and surfaces structured errors per stage.

## Technical Context

**Language/Version**: Python 3.11 (backend), Node.js 20 LTS (frontend), TypeScript 5.x  
**Primary Dependencies**: FastAPI, Pydantic, Uvicorn, uv, Ruff  
**Storage**: N/A (no persistence)  
**Testing**: pytest for orchestration flow and error paths  
**Target Platform**: Local developer machines (macOS/Linux/Windows)  
**Project Type**: Web (backend + frontend)  
**Performance Goals**: End-to-end completion within 15 seconds for short input  
**Constraints**: WAV input/output; no auth; no persistence  
**Scale/Scope**: Single orchestration endpoint and health check

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

- Decision: WAV-only input and output.  
  Rationale: Aligns with existing STT/TTS defaults and keeps pipeline simple.  
  Alternatives considered: WAV+MP3.
- Decision: Sequential orchestration (no parallelism).  
  Rationale: Matches requirement and reduces complexity.  
  Alternatives considered: Parallel prefetching.

## Phase 1: Design & Contracts

### Data Model

Documented in `/home/relu/misc/local-voice-assistant-codex/specs/001-orchestrator/data-model.md`.

### API Contracts

OpenAPI contract for orchestration and health endpoints in
`/home/relu/misc/local-voice-assistant-codex/specs/001-orchestrator/contracts/orchestrator.openapi.yaml`.

### Quickstart

Developer setup and run steps captured in
`/home/relu/misc/local-voice-assistant-codex/specs/001-orchestrator/quickstart.md`.

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
specs/001-orchestrator/
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
│   │   └── orchestrator.py
│   ├── services/
│   │   └── orchestrator.py
│   └── main.py
├── tests/
│   ├── test_health.py
│   └── test_orchestrator.py
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
