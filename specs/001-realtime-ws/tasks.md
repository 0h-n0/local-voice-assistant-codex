# Tasks: Realtime Voice WebSocket

**Input**: Design documents from `/specs/001-realtime-ws/`
**Prerequisites**: plan.md (required), spec.md (required for user stories), research.md, data-model.md, contracts/

**Tests**: Required for streaming critical paths per constitution.

**Organization**: Tasks are grouped by user story to enable independent implementation and testing of each story.

## Format: `[ID] [P?] [Story] Description`

- **[P]**: Can run in parallel (different files, no dependencies)
- **[Story]**: Which user story this task belongs to (e.g., US1, US2, US3)
- Include exact file paths in descriptions

## Phase 1: Setup (Shared Infrastructure)

**Purpose**: Project initialization and basic structure

- [ ] T001 Add WebSocket event types in backend/app/schemas/realtime_ws.py
- [ ] T002 Add frontend stream event types in frontend/app/services/realtimeTypes.ts

---

## Phase 2: Foundational (Blocking Prerequisites)

**Purpose**: Core infrastructure that MUST be complete before ANY user story can be implemented

**⚠️ CRITICAL**: No user story work can begin until this phase is complete

- [ ] T003 Create WebSocket service handler in backend/app/services/realtime_ws.py
- [ ] T004 Add WebSocket route in backend/app/api/realtime_ws.py
- [ ] T005 Register WebSocket route in backend/app/main.py
- [ ] T006 Create frontend WebSocket client wrapper in frontend/app/services/realtimeClient.ts

**Checkpoint**: Foundation ready - user story implementation can now begin

---

## Phase 3: User Story 1 - Live Voice Stream (Priority: P1) 🎯 MVP

**Goal**: Stream audio frames and show partial transcript updates in real time.

**Independent Test**: Stream frames and verify partial transcript events appear in UI.

### Tests for User Story 1 (REQUIRED) ⚠️

- [ ] T007 [P] [US1] Add backend WebSocket stream test in backend/tests/test_realtime_ws_stream.py
- [ ] T008 [P] [US1] Add frontend stream update test in frontend/tests/realtimeTranscript.test.tsx

### Implementation for User Story 1

- [ ] T009 [US1] Emit partial transcript events in backend/app/services/realtime_ws.py
- [ ] T010 [US1] Handle transcript events in frontend/app/page.tsx
- [ ] T011 [US1] Show live transcript updates in frontend/app/components/ChatMessage.tsx

**Checkpoint**: User Story 1 functional and testable independently

---

## Phase 4: User Story 2 - Live Response Playback (Priority: P2)

**Goal**: Emit response text and audio frames for playback with explicit user action.

**Independent Test**: Receive response event and play audio after user action.

### Tests for User Story 2 (REQUIRED) ⚠️

- [ ] T012 [P] [US2] Add response event test in backend/tests/test_realtime_ws_response.py
- [ ] T013 [P] [US2] Add playback UI test in frontend/tests/realtimePlayback.test.tsx

### Implementation for User Story 2

- [ ] T014 [US2] Emit response and audio events in backend/app/services/realtime_ws.py
- [ ] T015 [US2] Add playback UI for audio events in frontend/app/components/PlaybackControls.tsx
- [ ] T016 [US2] Wire response events in frontend/app/page.tsx

**Checkpoint**: User Stories 1 and 2 work independently

---

## Phase 5: User Story 3 - Stream Status Feedback (Priority: P3)

**Goal**: Display recording/transcribing/responding status updates.

**Independent Test**: Send status events and verify UI state changes.

### Tests for User Story 3 (REQUIRED) ⚠️

- [ ] T017 [P] [US3] Add status event test in backend/tests/test_realtime_ws_status.py
- [ ] T018 [P] [US3] Add status UI test in frontend/tests/realtimeStatus.test.tsx

### Implementation for User Story 3

- [ ] T019 [US3] Emit status events in backend/app/services/realtime_ws.py
- [ ] T020 [US3] Display status indicator in frontend/app/components/RecordingIndicator.tsx
- [ ] T021 [US3] Wire status handling in frontend/app/page.tsx

**Checkpoint**: All user stories independently functional

---

## Phase 6: Polish & Cross-Cutting Concerns

**Purpose**: Improvements that affect multiple user stories

- [ ] T022 [P] Update README with WebSocket usage in README.md
- [ ] T023 Run quickstart validation from specs/001-realtime-ws/quickstart.md

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
- Backend events before frontend handling
- Story complete before moving to next priority

### Parallel Opportunities

- T007 and T008 can run in parallel
- T012 and T013 can run in parallel
- T017 and T018 can run in parallel
- T022 can run in parallel with implementation work

---

## Parallel Example: User Story 1

```bash
Task: "Add backend WebSocket stream test in backend/tests/test_realtime_ws_stream.py"
Task: "Add frontend stream update test in frontend/tests/realtimeTranscript.test.tsx"
```

---

## Implementation Strategy

### MVP First (User Story 1 Only)

1. Complete Phase 1: Setup
2. Complete Phase 2: Foundational
3. Complete Phase 3: User Story 1
4. **STOP and VALIDATE**: Test User Story 1 independently

### Incremental Delivery

1. Setup + Foundational → Foundation ready
2. Add User Story 1 → Test independently → MVP ready
3. Add User Story 2 → Test independently
4. Add User Story 3 → Test independently
5. Finish Polish tasks
