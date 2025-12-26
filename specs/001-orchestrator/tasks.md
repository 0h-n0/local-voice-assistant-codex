---

description: "Task list for Voice Orchestrator implementation"
---

# Tasks: Voice Orchestrator

**Input**: Design documents from `/specs/001-orchestrator/`
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

- [X] T001 Add orchestrator configuration in `backend/app/config.py`
- [X] T002 [P] Create orchestration service in `backend/app/services/orchestrator.py`
- [X] T003 Ensure uv lockfile is up to date in `backend/uv.lock`

---

## Phase 2: Foundational (Blocking Prerequisites)

**Purpose**: Shared foundation needed before user stories

- [X] T004 Create orchestrator API router in `backend/app/api/orchestrator.py`
- [X] T005 Register orchestrator router in `backend/app/main.py`

**Checkpoint**: Foundation ready - user story implementation can now begin in parallel

---

## Phase 3: User Story 1 - End-to-End Voice Flow (Priority: P1) 🎯 MVP

**Goal**: Run STT → LLM → TTS end-to-end and return WAV output

**Independent Test**: Submit WAV input and receive WAV output

### Tests for User Story 1 (REQUIRED) ⚠️

- [X] T006 [P] [US1] Add orchestration flow tests in `backend/tests/test_orchestrator_flow.py`

### Implementation for User Story 1

- [X] T007 [US1] Implement request schema in `backend/app/schemas/orchestrator.py`
- [X] T008 [US1] Implement orchestration endpoint in `backend/app/api/orchestrator.py`
- [X] T009 [US1] Implement STT → LLM → TTS calls in `backend/app/services/orchestrator.py`

**Checkpoint**: User Story 1 should be complete and independently usable

---

## Phase 4: User Story 2 - Orchestration Error Handling (Priority: P2)

**Goal**: Surface structured errors from each stage

**Independent Test**: Simulate stage failures and receive structured errors

### Tests for User Story 2 (REQUIRED) ⚠️

- [X] T010 [P] [US2] Add stage error tests in `backend/tests/test_orchestrator_errors.py`

### Implementation for User Story 2

- [X] T011 [US2] Add stage error schema in `backend/app/schemas/errors.py`
- [X] T012 [US2] Map stage failures to error responses in `backend/app/api/orchestrator.py`

**Checkpoint**: User Story 2 should be complete and independently usable

---

## Phase 5: User Story 3 - Operational Visibility (Priority: P3)

**Goal**: Provide health checks and safe logging

**Independent Test**: Health returns ok and logs indicate failing stage

### Tests for User Story 3 (REQUIRED) ⚠️

- [X] T013 [P] [US3] Add health endpoint tests in `backend/tests/test_health.py`

### Implementation for User Story 3

- [X] T014 [US3] Implement health endpoint in `backend/app/api/health.py`
- [X] T015 [US3] Add logging without audio content in `backend/app/api/orchestrator.py`

**Checkpoint**: Operational visibility requirements are satisfied

---

## Phase N: Polish & Cross-Cutting Concerns

**Purpose**: Documentation and UX refinements

- [X] T016 Update README with orchestrator usage in `README.md`
- [X] T017 Update quickstart examples in `specs/001-orchestrator/quickstart.md`

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

- T002 can run in parallel with schema creation
- T006 can run in parallel with schema creation
- T010 and T013 can run in parallel

---

## Parallel Example: User Story 1

```bash
Task: "Add orchestration flow tests in backend/tests/test_orchestrator_flow.py"
Task: "Implement request schema in backend/app/schemas/orchestrator.py"
```

---

## Implementation Strategy

### MVP First (User Story 1 Only)

1. Complete Phase 1: Setup
2. Complete Phase 2: Foundational
3. Complete Phase 3: User Story 1
4. **STOP and VALIDATE**: WAV input returns WAV output

### Incremental Delivery

1. Complete Setup + Foundational
2. Add User Story 1 → Validate orchestration
3. Add User Story 2 → Validate errors
4. Add User Story 3 → Validate health/logging
5. Finish with Polish tasks
