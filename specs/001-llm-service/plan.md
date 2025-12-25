# Implementation Plan: LLM Service

**Branch**: `001-llm-service` | **Date**: 2025-12-25 | **Spec**: /home/relu/misc/local-voice-assistant-codex/specs/001-llm-service/spec.md
**Input**: Feature specification from `/specs/001-llm-service/spec.md`

## Summary

Build a FastAPI service that accepts text prompts, queries OpenAI gpt-5-mini, and
returns a single non-streaming response with structured error handling and a
health check endpoint.

## Technical Context

**Language/Version**: Python 3.11 (backend), Node.js 20 LTS (frontend), TypeScript 5.x  
**Primary Dependencies**: FastAPI, Pydantic, Uvicorn, uv, Ruff, OpenAI API client  
**Storage**: N/A (no persistence)  
**Testing**: pytest for API endpoints and error handling  
**Target Platform**: Local developer machines (macOS/Linux/Windows)  
**Project Type**: Web (backend + frontend)  
**Performance Goals**: Response within 5 seconds for short prompts  
**Constraints**: Non-streaming responses; no auth; no persistence  
**Scale/Scope**: Single service API for prompt → response

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

- Decision: Use OpenAI gpt-5-mini for prompt completion.  
  Rationale: Explicitly requested provider/model.  
  Alternatives considered: Other OpenAI models.
- Decision: Non-streaming responses.  
  Rationale: Simplifies integration and aligns with clarified requirement.  
  Alternatives considered: Streaming responses.
- Decision: 4,000 character prompt limit.  
  Rationale: Keeps requests bounded and predictable.  
  Alternatives considered: 1,000, 8,000.
- Decision: No persistence of prompts/responses.  
  Rationale: Aligns with privacy constraints and reduces risk.  
  Alternatives considered: Short-term logging.

## Phase 1: Design & Contracts

### Data Model

Documented in `/home/relu/misc/local-voice-assistant-codex/specs/001-llm-service/data-model.md`.

### API Contracts

OpenAPI contract for prompt completion and health endpoints in
`/home/relu/misc/local-voice-assistant-codex/specs/001-llm-service/contracts/llm.openapi.yaml`.

### Quickstart

Developer setup and run steps captured in
`/home/relu/misc/local-voice-assistant-codex/specs/001-llm-service/quickstart.md`.

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
specs/001-llm-service/
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
│   │   └── llm.py
│   ├── services/
│   │   └── llm_client.py
│   └── main.py
├── tests/
│   ├── test_health.py
│   └── test_llm.py
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
