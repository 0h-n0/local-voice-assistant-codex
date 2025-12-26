# Tasks: Conversation History Storage

**Input**: Design documents from `/specs/001-conversation-storage/`
**Prerequisites**: plan.md (required), spec.md (required for user stories), research.md, data-model.md, contracts/

**Tests**: Required for persistence and API critical paths per constitution.

**Organization**: Tasks are grouped by user story to enable independent implementation and testing of each story.

## Format: `[ID] [P?] [Story] Description`

- **[P]**: Can run in parallel (different files, no dependencies)
- **[Story]**: Which user story this task belongs to (e.g., US1, US2, US3)
- Include exact file paths in descriptions

## Phase 1: Setup (Shared Infrastructure)

**Purpose**: Project initialization and basic structure

- [X] T001 Add SQLite storage configuration defaults in backend/app/config.py
- [X] T002 Create SQLite connection + schema initializer in backend/app/services/conversation_db.py

---

## Phase 2: Foundational (Blocking Prerequisites)

**Purpose**: Core infrastructure that MUST be complete before ANY user story can be implemented

**⚠️ CRITICAL**: No user story work can begin until this phase is complete

- [X] T003 Add conversation/message schemas in backend/app/schemas/conversations.py
- [X] T004 Implement conversation store base class in backend/app/services/conversation_store.py
- [X] T005 Add conversations router skeleton in backend/app/api/conversations.py
- [X] T006 Register conversations router in backend/app/main.py

**Checkpoint**: Foundation ready - user story implementation can now begin

---

## Phase 3: User Story 1 - Save Conversation Messages (Priority: P1) 🎯 MVP

**Goal**: Append messages to a conversation and retrieve full history.

**Independent Test**: Append multiple messages and retrieve the conversation to verify
order, roles, and timestamps.

### Tests for User Story 1 (REQUIRED) ⚠️

- [X] T007 [P] [US1] Add append messages test in backend/tests/test_conversations_append.py
- [X] T008 [P] [US1] Add get conversation test in backend/tests/test_conversations_get.py

### Implementation for User Story 1

- [X] T009 [US1] Implement append messages handler in backend/app/api/conversations.py
- [X] T010 [US1] Implement get conversation handler in backend/app/api/conversations.py
- [X] T011 [US1] Wire append/get methods in backend/app/services/conversation_store.py
- [X] T012 [US1] Add response/error models in backend/app/schemas/conversations.py

**Checkpoint**: User Story 1 functional and testable independently

---

## Phase 4: User Story 2 - List Conversations (Priority: P2)

**Goal**: List conversation summaries with identifiers and updated timestamps.

**Independent Test**: Create multiple conversations and verify list ordering and contents.

### Tests for User Story 2 (REQUIRED) ⚠️

- [X] T013 [P] [US2] Add list conversations test in backend/tests/test_conversations_list.py

### Implementation for User Story 2

- [X] T014 [US2] Implement list conversations handler in backend/app/api/conversations.py
- [X] T015 [US2] Implement list logic in backend/app/services/conversation_store.py
- [X] T016 [US2] Add list response schema in backend/app/schemas/conversations.py

**Checkpoint**: User Stories 1 and 2 work independently

---

## Phase 5: User Story 3 - Remove Conversations (Priority: P3)

**Goal**: Delete a conversation and its messages with clear not-found handling.

**Independent Test**: Delete a conversation and ensure it no longer appears in list or get.

### Tests for User Story 3 (REQUIRED) ⚠️

- [X] T017 [P] [US3] Add delete conversation test in backend/tests/test_conversations_delete.py
- [X] T018 [P] [US3] Add delete-not-found test in backend/tests/test_conversations_delete.py

### Implementation for User Story 3

- [X] T019 [US3] Implement delete conversation handler in backend/app/api/conversations.py
- [X] T020 [US3] Implement delete logic in backend/app/services/conversation_store.py
- [X] T021 [US3] Add delete response handling in backend/app/schemas/conversations.py

**Checkpoint**: All user stories independently functional

---

## Phase 6: Polish & Cross-Cutting Concerns

**Purpose**: Improvements that affect multiple user stories

- [X] T022 [P] Update README with conversation API usage in README.md
- [ ] T023 Run quickstart validation from specs/001-conversation-storage/quickstart.md

---

## Dependencies & Execution Order

### Phase Dependencies

- **Setup (Phase 1)**: No dependencies - can start immediately
- **Foundational (Phase 2)**: Depends on Setup completion - BLOCKS all user stories
- **User Stories (Phase 3+)**: All depend on Foundational phase completion
  - User stories can then proceed in parallel (if staffed)
  - Or sequentially in priority order (P1 → P2 → P3)
- **Polish (Final Phase)**: Depends on all desired user stories being complete

### User Story Dependencies

- **User Story 1 (P1)**: Can start after Foundational (Phase 2) - No dependencies
- **User Story 2 (P2)**: Can start after Foundational (Phase 2) - Independent of US1
- **User Story 3 (P3)**: Can start after Foundational (Phase 2) - Independent of US1/US2

### Within Each User Story

- Tests MUST be written and FAIL before implementation
- Schemas before services
- Services before endpoints
- Story complete before moving to next priority

### Parallel Opportunities

- T007 and T008 can run in parallel (different test files)
- T013 can run in parallel with other story tests once foundations are ready
- T017 and T018 can run in parallel within the same test file if coordinated
- Documentation updates (T022) can run in parallel with implementation

---

## Parallel Example: User Story 1

```bash
Task: "Add append messages test in backend/tests/test_conversations_append.py"
Task: "Add get conversation test in backend/tests/test_conversations_get.py"
```

---

## Implementation Strategy

### MVP First (User Story 1 Only)

1. Complete Phase 1: Setup
2. Complete Phase 2: Foundational
3. Complete Phase 3: User Story 1
4. **STOP and VALIDATE**: Run tests for US1

### Incremental Delivery

1. Setup + Foundational → Foundation ready
2. Add User Story 1 → Test independently → MVP ready
3. Add User Story 2 → Test independently
4. Add User Story 3 → Test independently
5. Finish Polish tasks
