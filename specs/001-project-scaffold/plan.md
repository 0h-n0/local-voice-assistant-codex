# Implementation Plan: Project Scaffold

**Branch**: `001-project-scaffold` | **Date**: 2025-12-25 | **Spec**: /home/relu/misc/local-voice-assistant-codex/specs/001-project-scaffold/spec.md
**Input**: Feature specification from `/specs/001-project-scaffold/spec.md`

## Summary

Create a single-repository scaffold with a FastAPI backend and Next.js frontend,
including local run instructions, a minimal health endpoint, a static status
page, and quality checks that align with the constitution.

## Technical Context

**Language/Version**: Python 3.11 (backend), Node.js 20 LTS (frontend), TypeScript 5.x  
**Primary Dependencies**: FastAPI, Pydantic, Uvicorn, uv, Ruff, Next.js, React  
**Storage**: N/A (no persistence in scaffold)  
**Testing**: pytest for backend health endpoint; no frontend tests in scaffold  
**Target Platform**: Local developer machines (macOS/Linux/Windows)  
**Project Type**: Web (backend + frontend)  
**Performance Goals**: N/A for scaffold (local dev baseline)  
**Constraints**: Offline-first setup; no auth; no external services  
**Scale/Scope**: Single repository scaffold for two services

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

- Decision: Python 3.11 for the backend.  
  Rationale: Stable, widely supported by FastAPI and uv tooling.  
  Alternatives considered: Python 3.10, Python 3.12.
- Decision: Node.js 20 LTS for the frontend.  
  Rationale: Current LTS with broad Next.js compatibility.  
  Alternatives considered: Node.js 18 LTS.
- Decision: pytest for the backend health endpoint test only.  
  Rationale: Minimal critical-path coverage without introducing extra tooling.  
  Alternatives considered: unittest, no tests.
- Decision: No database or external services in the scaffold.  
  Rationale: Keeps the scaffold offline and minimal.  
  Alternatives considered: SQLite, local cache.

## Phase 1: Design & Contracts

### Data Model

Documented in `/home/relu/misc/local-voice-assistant-codex/specs/001-project-scaffold/data-model.md`.

### API Contracts

OpenAPI contract for the health endpoint in
`/home/relu/misc/local-voice-assistant-codex/specs/001-project-scaffold/contracts/health.openapi.yaml`.

### Quickstart

Developer setup and run steps captured in
`/home/relu/misc/local-voice-assistant-codex/specs/001-project-scaffold/quickstart.md`.

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
specs/001-project-scaffold/
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
│   │   └── health.py
│   └── main.py
├── tests/
│   └── test_health.py
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

**Structure Decision**: Single repository with `backend/` and `frontend/` top-level
folders to keep setup and documentation centralized.

## Complexity Tracking

No constitution violations requiring justification.
