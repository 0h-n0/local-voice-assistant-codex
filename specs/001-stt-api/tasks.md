---

description: "Task list for STT API implementation"
---

# Tasks: STT API

**Input**: Design documents from `/specs/001-stt-api/`
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

- [X] T001 Verify backend dependencies in `backend/pyproject.toml` for FastAPI, Pydantic, and model runtime
- [X] T002 [P] Add STT configuration defaults in `backend/app/config.py`
- [X] T003 [P] Create model loader module in `backend/app/services/model_loader.py`
- [X] T004 Ensure uv lockfile is up to date in `backend/uv.lock`

---

## Phase 2: Foundational (Blocking Prerequisites)

**Purpose**: Shared foundation needed before user stories

- [X] T005 Create STT service interface in `backend/app/services/transcription.py`
- [X] T006 Add API router base in `backend/app/api/stt.py`
- [X] T007 Register STT router in `backend/app/main.py`

**Checkpoint**: Foundation ready - user story implementation can now begin in parallel

---

## Phase 3: User Story 1 - Transcribe Audio File (Priority: P1) 🎯 MVP

**Goal**: Accept Japanese audio files and return transcribed text

**Independent Test**: Upload a WAV/FLAC/MP3 sample and verify plain text output

### Tests for User Story 1 (REQUIRED) ⚠️

- [X] T008 [P] [US1] Add file transcription tests in `backend/tests/test_stt_file.py`

### Implementation for User Story 1

- [X] T009 [US1] Implement file upload endpoint in `backend/app/api/stt.py`
- [X] T010 [US1] Implement file decoding and validation in `backend/app/services/transcription.py`
- [X] T011 [US1] Add response schema in `backend/app/schemas/stt.py`

**Checkpoint**: User Story 1 should be complete and independently usable

---

## Phase 4: User Story 2 - Transcribe Microphone Input (Priority: P2)

**Goal**: Stream microphone input via WebSocket and return transcription

**Independent Test**: Send short audio frames and receive a final text response

### Tests for User Story 2 (REQUIRED) ⚠️

- [X] T012 [P] [US2] Add WebSocket streaming tests in `backend/tests/test_stt_stream.py`

### Implementation for User Story 2

- [X] T013 [US2] Implement WebSocket handler in `backend/app/api/stt.py`
- [X] T014 [US2] Add streaming decode/aggregation logic in `backend/app/services/transcription.py`

**Checkpoint**: User Story 2 should be functional for streaming input

---

## Phase 5: User Story 3 - Operational Visibility (Priority: P3)

**Goal**: Provide health checks and structured errors

**Independent Test**: Health endpoint returns ok and errors are structured

### Tests for User Story 3 (REQUIRED) ⚠️

- [X] T015 [P] [US3] Add health endpoint tests in `backend/tests/test_health.py`
- [X] T016 [P] [US3] Add error response tests in `backend/tests/test_errors.py`

### Implementation for User Story 3

- [X] T017 [US3] Implement health endpoint in `backend/app/api/health.py`
- [X] T018 [US3] Add error schema and mapping in `backend/app/schemas/errors.py`

**Checkpoint**: Operational visibility requirements are satisfied

---

## Phase N: Polish & Cross-Cutting Concerns

**Purpose**: Documentation and UX refinements

- [X] T019 Update README with STT API usage in `README.md`
- [X] T020 Update quickstart examples in `specs/001-stt-api/quickstart.md`

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
- T008 and schema creation can run in parallel if files do not overlap
- T012 and T015/T016 can run in parallel

---

## Parallel Example: User Story 2

```bash
Task: "Add WebSocket streaming tests in backend/tests/test_stt_stream.py"
Task: "Implement WebSocket handler in backend/app/api/stt.py"
```

---

## Implementation Strategy

### MVP First (User Story 1 Only)

1. Complete Phase 1: Setup
2. Complete Phase 2: Foundational
3. Complete Phase 3: User Story 1
4. **STOP and VALIDATE**: File transcription works for WAV/FLAC/MP3

### Incremental Delivery

1. Complete Setup + Foundational
2. Add User Story 1 → Validate file transcription
3. Add User Story 2 → Validate WebSocket streaming
4. Add User Story 3 → Validate health/errors
5. Finish with Polish tasks
