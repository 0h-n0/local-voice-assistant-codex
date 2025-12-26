# Implementation Plan: Voice Chat Web UI

**Branch**: `001-voice-chat-ui` | **Date**: 2025-12-27 | **Spec**: /home/relu/misc/local-voice-assistant-codex/specs/001-voice-chat-ui/spec.md
**Input**: Feature specification from `/specs/001-voice-chat-ui/spec.md`

**Note**: This template is filled in by the `/speckit.plan` command. See `.specify/templates/commands/plan.md` for the execution workflow.

## Summary

Implement a ChatGPT-style web UI with a single active conversation view, voice
recording controls, and explicit audio playback for assistant responses. The UI
presents a chronological transcript, shows a recording indicator during capture,
and clears history on reload.

## Technical Context

**Language/Version**: TypeScript (frontend), Python 3.11 (backend)
**Primary Dependencies**: Next.js/React, FastAPI
**Storage**: N/A (UI consumes existing APIs)
**Testing**: frontend unit tests (e.g., Vitest) and backend pytest for integration
**Target Platform**: Modern desktop browsers
**Project Type**: web (frontend + backend)
**Performance Goals**: Voice prompt → response display in <10s
**Constraints**: Offline-first, explicit playback action, toggle recording, in-memory history
**Scale/Scope**: Single active conversation, local usage

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
specs/001-voice-chat-ui/
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
├── src/
│   ├── components/
│   ├── pages/
│   └── services/
└── tests/
```

**Structure Decision**: Use existing frontend/ for UI and backend/ for API support.

## Complexity Tracking

> **Fill ONLY if Constitution Check has violations that must be justified**

| Violation | Why Needed | Simpler Alternative Rejected Because |
|-----------|------------|-------------------------------------|
