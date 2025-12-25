---

description: "Task list for LLM Service implementation"
---

# Tasks: LLM Service

**Input**: Design documents from `/specs/001-llm-service/`
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

- [X] T001 Verify backend dependencies in `backend/pyproject.toml` for OpenAI client and FastAPI
- [X] T002 [P] Add LLM service configuration in `backend/app/config.py`
- [X] T003 [P] Create OpenAI client wrapper in `backend/app/services/llm_client.py`
- [X] T004 Ensure uv lockfile is up to date in `backend/uv.lock`

---

## Phase 2: Foundational (Blocking Prerequisites)

**Purpose**: Shared foundation needed before user stories

- [X] T005 Create LLM API router in `backend/app/api/llm.py`
- [X] T006 Register LLM router in `backend/app/main.py`

**Checkpoint**: Foundation ready - user story implementation can now begin in parallel

---

## Phase 3: User Story 1 - Generate Text Response (Priority: P1) 🎯 MVP

**Goal**: Accept prompts and return non-streaming responses

**Independent Test**: Submit a prompt and verify a text response is returned

### Tests for User Story 1 (REQUIRED) ⚠️

- [X] T007 [P] [US1] Add completion endpoint tests in `backend/tests/test_llm_complete.py`

### Implementation for User Story 1

- [X] T008 [US1] Implement request/response schemas in `backend/app/schemas/llm.py`
- [X] T009 [US1] Implement completion endpoint in `backend/app/api/llm.py`
- [X] T010 [US1] Implement prompt validation in `backend/app/api/llm.py`

**Checkpoint**: User Story 1 should be complete and independently usable

---

## Phase 4: User Story 2 - Handle Provider Errors (Priority: P2)

**Goal**: Return structured errors for upstream failures

**Independent Test**: Simulate provider error and receive structured response

### Tests for User Story 2 (REQUIRED) ⚠️

- [X] T011 [P] [US2] Add provider error tests in `backend/tests/test_llm_errors.py`

### Implementation for User Story 2

- [X] T012 [US2] Map provider failures to error responses in `backend/app/services/llm_client.py`
- [X] T013 [US2] Add error schema in `backend/app/schemas/errors.py`

**Checkpoint**: User Story 2 should be complete and independently usable

---

## Phase 5: User Story 3 - Operational Visibility (Priority: P3)

**Goal**: Provide health checks and safe logging

**Independent Test**: Health returns ok and logs omit prompt content

### Tests for User Story 3 (REQUIRED) ⚠️

- [X] T014 [P] [US3] Add health endpoint tests in `backend/tests/test_health.py`

### Implementation for User Story 3

- [X] T015 [US3] Implement health endpoint in `backend/app/api/health.py`
- [X] T016 [US3] Add logging without prompt content in `backend/app/api/llm.py`

**Checkpoint**: Operational visibility requirements are satisfied

---

## Phase N: Polish & Cross-Cutting Concerns

**Purpose**: Documentation and UX refinements

- [X] T017 Update README with LLM API usage in `README.md`
- [X] T018 Update quickstart examples in `specs/001-llm-service/quickstart.md`

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
- T011 and T014 can run in parallel

---

## Parallel Example: User Story 1

```bash
Task: "Add completion endpoint tests in backend/tests/test_llm_complete.py"
Task: "Implement request/response schemas in backend/app/schemas/llm.py"
```

---

## Implementation Strategy

### MVP First (User Story 1 Only)

1. Complete Phase 1: Setup
2. Complete Phase 2: Foundational
3. Complete Phase 3: User Story 1
4. **STOP and VALIDATE**: Prompt returns text response

### Incremental Delivery

1. Complete Setup + Foundational
2. Add User Story 1 → Validate completion
3. Add User Story 2 → Validate error handling
4. Add User Story 3 → Validate health/logging
5. Finish with Polish tasks
