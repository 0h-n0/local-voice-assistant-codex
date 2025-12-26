# Implementation Plan: Config Source Management

**Branch**: `001-add-config-env` | **Date**: 2025-09-28 | **Spec**: /home/relu/misc/local-voice-assistant-codex/specs/001-add-config-env/spec.md
**Input**: Feature specification from `/specs/001-add-config-env/spec.md`

## Summary

Provide centralized configuration management for API keys, model paths, and audio
settings using .env, environment variables, and a single config file with deterministic
precedence. Validate configuration at startup, redact sensitive values in summaries, and
expose a safe configuration summary endpoint for operators.

## Technical Context

**Language/Version**: Python 3.11
**Primary Dependencies**: FastAPI, Pydantic v2, uv, Ruff
**Storage**: Local config file and environment variables (no database)
**Testing**: pytest (backend), vitest (frontend)
**Target Platform**: Local Linux/macOS server
**Project Type**: Web application (frontend + backend)
**Performance Goals**: Configuration load and validation < 1s on startup
**Constraints**: Local-first, no external network access for config resolution
**Scale/Scope**: Single-device, single-operator runtime configuration

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

Post-design re-check: All items remain compliant after Phase 1 outputs.

## Project Structure

### Documentation (this feature)

```text
/home/relu/misc/local-voice-assistant-codex/specs/001-add-config-env/
├── plan.md
├── research.md
├── data-model.md
├── quickstart.md
├── contracts/
└── tasks.md
```

### Source Code (repository root)

```text
/home/relu/misc/local-voice-assistant-codex/backend/
├── app/
│   ├── api/
│   ├── config.py
│   ├── schemas/
│   └── services/
└── tests/

/home/relu/misc/local-voice-assistant-codex/frontend/
├── app/
│   ├── components/
│   ├── services/
│   └── page.tsx
└── tests/
```

**Structure Decision**: Web application with `backend/` and `frontend/` roots; backend
owns configuration loading and validation, frontend optionally consumes a redacted
summary endpoint.

## Phase 0: Outline & Research

### Unknowns and Research Tasks

- Confirm best practice for Pydantic v2 configuration loading with .env and a config
  file without extra dependencies.
- Decide config file format that avoids new dependencies and supports deterministic
  parsing.
- Define safe redaction strategy for sensitive values in summaries.

### Research Output

Write /home/relu/misc/local-voice-assistant-codex/specs/001-add-config-env/research.md
with decisions and rationale.

## Phase 1: Design & Contracts

### Data Model

Write /home/relu/misc/local-voice-assistant-codex/specs/001-add-config-env/data-model.md
capturing configuration setting metadata, source, and sensitivity flags.

### API Contracts

Create /home/relu/misc/local-voice-assistant-codex/specs/001-add-config-env/contracts/
with an OpenAPI contract for a redacted configuration summary endpoint.

### Quickstart

Write /home/relu/misc/local-voice-assistant-codex/specs/001-add-config-env/quickstart.md
covering .env/config file setup and summary verification steps.

### Agent Context Update

Run:

```sh
/home/relu/misc/local-voice-assistant-codex/.specify/scripts/bash/update-agent-context.sh codex
```

## Phase 2: Task Planning

Tasks will be generated in `/specs/001-add-config-env/tasks.md` via `/speckit.tasks`.
