# Implementation Plan: Realtime Voice WebSocket

**Branch**: `001-realtime-ws` | **Date**: 2025-12-27 | **Spec**: /home/relu/misc/local-voice-assistant-codex/specs/001-realtime-ws/spec.md
**Input**: Feature specification from `/specs/001-realtime-ws/spec.md`

**Note**: This template is filled in by the `/speckit.plan` command. See `.specify/templates/commands/plan.md` for the execution workflow.

## Summary

Add a WebSocket streaming channel for real-time voice input, partial transcription
updates, response text, and audio frames. The UI will show live transcript updates,
status events, and provide explicit playback controls, with auto-reconnect and
100–200ms WAV chunk framing.

## Technical Context

**Language/Version**: TypeScript (frontend), Python 3.11 (backend)
**Primary Dependencies**: Next.js/React, FastAPI
**Storage**: N/A (streaming events only)
**Testing**: pytest (backend), frontend unit tests (Vitest)
**Target Platform**: Modern desktop browsers
**Project Type**: web (frontend + backend)
**Performance Goals**: Partial transcript within 1s; final response within 5s of end
**Constraints**: Offline-first; token via Sec-WebSocket-Protocol; auto-reconnect restart
**Scale/Scope**: Single-user local session; WAV frames 100–200ms

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

## Project Structure

### Documentation (this feature)

```text
specs/001-realtime-ws/
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
│   ├── schemas/
│   └── services/
└── tests/

frontend/
├── app/
│   ├── components/
│   └── services/
└── tests/
```

**Structure Decision**: Use existing frontend/ and backend/ layout.

## Complexity Tracking

> **Fill ONLY if Constitution Check has violations that must be justified**

| Violation | Why Needed | Simpler Alternative Rejected Because |
|-----------|------------|-------------------------------------|
