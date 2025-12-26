---

description: "Task list for TTS API implementation"
---

# Tasks: TTS API

**Input**: Design documents from `/specs/001-tts-api/`
**Prerequisites**: plan.md (required), spec.md (required), research.md, data-model.md, contracts/, quickstart.md

**Tests**: Tests are REQUIRED for critical API paths per constitution.

**Organization**: Tasks are grouped by user story to enable independent implementation and testing of each story.

## Format: `[ID] [P?] [Story] Description`

- **[P]**: Can run in parallel (different files, no dependencies)
- **[Story]**: Which user story this task belongs to (e.g., US1, US2, US3)
- Include exact file paths in descriptions

## Path Conventions

- **Web app**: `backend/`, `frontend/` at repository root

## Phase 1: Setup (Shared Infrastructure)

**Purpose**: Project initialization and basic structure

- [X] T001 Verify backend dependencies in `backend/pyproject.toml` for Style-Bert-VITS2 runtime
- [X] T002 [P] Add TTS configuration defaults in `backend/app/config.py`
- [X] T003 [P] Create TTS engine wrapper in `backend/app/services/tts_engine.py`
- [X] T004 Ensure uv lockfile is up to date in `backend/uv.lock`

---

## Phase 2: Foundational (Blocking Prerequisites)

**Purpose**: Shared foundation needed before user stories

- [X] T005 Create TTS API router in `backend/app/api/tts.py`
- [X] T006 Register TTS router in `backend/app/main.py`

**Checkpoint**: Foundation ready - user story implementation can now begin in parallel

---

## Phase 3: User Story 1 - Text to Speech Conversion (Priority: P1) 🎯 MVP

**Goal**: Accept Japanese text and return WAV audio

**Independent Test**: Submit a prompt and receive WAV audio output

### Tests for User Story 1 (REQUIRED) ⚠️

- [X] T007 [P] [US1] Add synthesis endpoint tests in `backend/tests/test_tts_synthesize.py`

### Implementation for User Story 1

- [X] T008 [US1] Implement request schema in `backend/app/schemas/tts.py`
- [X] T009 [US1] Implement synthesis endpoint in `backend/app/api/tts.py`
- [X] T010 [US1] Implement text validation and audio generation in `backend/app/services/tts_engine.py`

**Checkpoint**: User Story 1 should be complete and independently usable

---

## Phase 4: User Story 2 - Voice Configuration (Priority: P2)

**Goal**: Support voice/style selection

**Independent Test**: Request synthesis with different voices and verify outputs differ

### Tests for User Story 2 (REQUIRED) ⚠️

- [X] T011 [P] [US2] Add voice selection tests in `backend/tests/test_tts_voice.py`

### Implementation for User Story 2

- [X] T012 [US2] Add voice selection handling in `backend/app/services/tts_engine.py`
- [X] T013 [US2] Validate voice option in `backend/app/api/tts.py`

**Checkpoint**: User Story 2 should be complete and independently usable

---

## Phase 5: User Story 3 - Operational Visibility (Priority: P3)

**Goal**: Provide health checks and structured errors

**Independent Test**: Health returns ok and errors are structured

### Tests for User Story 3 (REQUIRED) ⚠️

- [X] T014 [P] [US3] Add health endpoint tests in `backend/tests/test_health.py`
- [X] T015 [P] [US3] Add error response tests in `backend/tests/test_tts_errors.py`

### Implementation for User Story 3

- [X] T016 [US3] Implement health endpoint in `backend/app/api/health.py`
- [X] T017 [US3] Add error schema and mapping in `backend/app/schemas/errors.py`

**Checkpoint**: Operational visibility requirements are satisfied

---

## Phase N: Polish & Cross-Cutting Concerns

**Purpose**: Documentation and UX refinements

- [X] T018 Update README with TTS API usage in `README.md`
- [X] T019 Update quickstart examples in `specs/001-tts-api/quickstart.md`

---

## Dependencies & Execution Order

### Phase Dependencies

- **Setup (Phase 1)**: No dependencies - can start immediately
- **Foundational (Phase 2)**: Depends on Setup completion - BLOCKS all user stories
- **User Stories (Phase 3+)**: Depend on Foundational phase completion
- **Polish (Final Phase)**: Depends on all desired user stories being complete

### User Story Dependencies

- **User Story 1 (P1)**: Can start after Foundational (Phase 2)
- **User Story 2 (P2)**: Can start after Foundational (Phase 2)
- **User Story 3 (P3)**: Can start after Foundational (Phase 2)

### Parallel Opportunities

- T002 and T003 can run in parallel
- T007 can run in parallel with schema creation
- T011 and T014/T015 can run in parallel

---

## Parallel Example: User Story 1

```bash
Task: "Add synthesis endpoint tests in backend/tests/test_tts_synthesize.py"
Task: "Implement request schema in backend/app/schemas/tts.py"
```

---

## Implementation Strategy

### MVP First (User Story 1 Only)

1. Complete Phase 1: Setup
2. Complete Phase 2: Foundational
3. Complete Phase 3: User Story 1
4. **STOP and VALIDATE**: Synthesis returns WAV output

### Incremental Delivery

1. Complete Setup + Foundational
2. Add User Story 1 → Validate synthesis
3. Add User Story 2 → Validate voice selection
4. Add User Story 3 → Validate health/errors
5. Finish with Polish tasks
