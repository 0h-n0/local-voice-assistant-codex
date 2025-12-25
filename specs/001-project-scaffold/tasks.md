---

description: "Task list for Project Scaffold implementation"
---

# Tasks: Project Scaffold

**Input**: Design documents from `/specs/001-project-scaffold/`
**Prerequisites**: plan.md (required), spec.md (required), research.md, data-model.md, contracts/, quickstart.md

**Tests**: Tests are REQUIRED for the backend health endpoint per constitution.

**Organization**: Tasks are grouped by user story to enable independent implementation and testing of each story.

## Format: `[ID] [P?] [Story] Description`

- **[P]**: Can run in parallel (different files, no dependencies)
- **[Story]**: Which user story this task belongs to (e.g., US1, US2, US3)
- Include exact file paths in descriptions

## Path Conventions

- **Web app**: `backend/`, `frontend/` at repository root

## Phase 1: Setup (Shared Infrastructure)

**Purpose**: Project initialization and basic structure

- [X] T001 Create repo structure per plan at `backend/`, `backend/app/`, `backend/app/api/`, `backend/tests/`, `frontend/`, `frontend/app/`, `frontend/public/`
- [X] T002 Initialize backend dependencies with uv in `backend/pyproject.toml`
- [X] T003 [P] Initialize frontend dependencies in `frontend/package.json`
- [X] T004 [P] Add Next.js TypeScript config in `frontend/tsconfig.json` and `frontend/next.config.js`
- [X] T005 Generate `backend/uv.lock` via `uv sync`

---

## Phase 2: Foundational (Blocking Prerequisites)

**Purpose**: Shared foundation needed before user stories

- [X] T006 Create FastAPI app entrypoint in `backend/app/main.py`
- [X] T007 Create API package marker in `backend/app/api/__init__.py`

**Checkpoint**: Foundation ready - user story implementation can now begin in parallel

---

## Phase 3: User Story 1 - Base Project Layout (Priority: P1) 🎯 MVP

**Goal**: Provide a clear, documented repository layout for onboarding

**Independent Test**: Verify README describes structure and setup at a glance

### Implementation for User Story 1

- [X] T008 [US1] Add project overview and layout summary in `README.md`
- [X] T009 [US1] Document repository structure and directories in `README.md`

**Checkpoint**: User Story 1 should be complete and independently usable

---

## Phase 4: User Story 2 - Local Run Verification (Priority: P2)

**Goal**: Provide a runnable local baseline with health endpoint and status page

**Independent Test**: Start both services and confirm health/status responses

### Implementation for User Story 2

- [X] T010 [US2] Implement health endpoint in `backend/app/api/health.py`
- [X] T011 [US2] Register health endpoint in `backend/app/main.py`
- [X] T012 [US2] Add static status page in `frontend/app/page.tsx`
- [X] T013 [US2] Add local run instructions for backend and frontend in `README.md`

**Checkpoint**: User Story 2 should be runnable end-to-end

---

## Phase 5: User Story 3 - Quality Checks (Priority: P3)

**Goal**: Provide standardized quality checks for consistent validation

**Independent Test**: Run lint/tests and confirm clear pass/fail output

### Tests for User Story 3 (REQUIRED by constitution) ⚠️

- [X] T014 [P] [US3] Add Ruff configuration in `backend/pyproject.toml`
- [X] T015 [US3] Add health endpoint test in `backend/tests/test_health.py`

### Implementation for User Story 3

- [X] T016 [US3] Document quality check commands in `README.md`

**Checkpoint**: Quality checks are documented and executable

---

## Phase N: Polish & Cross-Cutting Concerns

**Purpose**: Final documentation polish and consistency

- [X] T017 Update README with quickstart reference in `README.md`

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

- T003 and T004 can run in parallel
- T014 can run in parallel with documentation tasks
- User Story 1 and User Story 2 tasks can proceed in parallel after Phase 2

---

## Parallel Example: User Story 2

```bash
Task: "Implement health endpoint in backend/app/api/health.py"
Task: "Add static status page in frontend/app/page.tsx"
```

---

## Implementation Strategy

### MVP First (User Story 1 Only)

1. Complete Phase 1: Setup
2. Complete Phase 2: Foundational
3. Complete Phase 3: User Story 1
4. **STOP and VALIDATE**: Review README structure

### Incremental Delivery

1. Complete Setup + Foundational
2. Add User Story 1 → Validate documentation
3. Add User Story 2 → Validate local run
4. Add User Story 3 → Validate quality checks
5. Finish with Polish tasks
