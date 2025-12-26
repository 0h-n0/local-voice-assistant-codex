# Implementation Plan: One-Command Service Startup

**Branch**: `001-one-command-start` | **Date**: 2025-09-28 | **Spec**: /home/relu/misc/local-voice-assistant-codex/specs/001-one-command-start/spec.md
**Input**: Feature specification from `/specs/001-one-command-start/spec.md`

## Summary

Provide a one-command local startup workflow using docker-compose plus a Makefile
wrapper. Include start/stop/status commands, document the default service set, and
ensure idempotent behavior with clear error reporting for missing prerequisites or port
conflicts.

## Technical Context

**Language/Version**: Python 3.11, Node.js 18+
**Primary Dependencies**: FastAPI, React/Next (TypeScript), uv, Ruff, docker-compose
**Storage**: Local filesystem and SQLite (existing components)
**Testing**: pytest (backend), vitest (frontend)
**Target Platform**: Local Linux/macOS development environments
**Project Type**: Web application (frontend + backend)
**Performance Goals**: Startup completes within 2 minutes on typical laptops
**Constraints**: Local-first; single command must be idempotent; fail fast on
prerequisite/port issues
**Scale/Scope**: Single developer machine, local services only

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
/home/relu/misc/local-voice-assistant-codex/specs/001-one-command-start/
├── plan.md
├── research.md
├── data-model.md
├── quickstart.md
├── contracts/
└── tasks.md
```

### Source Code (repository root)

```text
/home/relu/misc/local-voice-assistant-codex/
├── backend/
├── frontend/
├── docker-compose.yml
└── Makefile
```

**Structure Decision**: Keep `backend/` and `frontend/` structure; add
`docker-compose.yml` and `Makefile` at repository root to orchestrate startup.

## Phase 0: Outline & Research

### Unknowns and Research Tasks

- Confirm best practice for docker-compose + Makefile workflow in local-only stacks.
- Decide default service list and their health checks for status reporting.
- Define idempotent behavior for start/stop/status commands.

### Research Output

Write /home/relu/misc/local-voice-assistant-codex/specs/001-one-command-start/research.md
with decisions and rationale.

## Phase 1: Design & Contracts

### Data Model

Write /home/relu/misc/local-voice-assistant-codex/specs/001-one-command-start/data-model.md
capturing service list and status representation.

### API Contracts

Create /home/relu/misc/local-voice-assistant-codex/specs/001-one-command-start/contracts/
with a contract for service status output (CLI/compose summary).

### Quickstart

Write /home/relu/misc/local-voice-assistant-codex/specs/001-one-command-start/quickstart.md
covering start/stop/status commands and expected output.

### Agent Context Update

Run:

```sh
/home/relu/misc/local-voice-assistant-codex/.specify/scripts/bash/update-agent-context.sh codex
```

## Phase 2: Task Planning

Tasks will be generated in `/specs/001-one-command-start/tasks.md` via `/speckit.tasks`.
