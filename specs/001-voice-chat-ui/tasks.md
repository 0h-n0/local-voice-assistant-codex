# Tasks: Voice Chat Web UI

**Input**: Design documents from `/specs/001-voice-chat-ui/`
**Prerequisites**: plan.md (required), spec.md (required for user stories), research.md, data-model.md, contracts/

**Tests**: Required for critical voice interaction paths.

**Organization**: Tasks are grouped by user story to enable independent implementation and testing of each story.

## Format: `[ID] [P?] [Story] Description`

- **[P]**: Can run in parallel (different files, no dependencies)
- **[Story]**: Which user story this task belongs to (e.g., US1, US2, US3)
- Include exact file paths in descriptions

## Phase 1: Setup (Shared Infrastructure)

**Purpose**: Project initialization and basic structure

- [X] T001 Add voice chat page route in frontend/app/page.tsx
- [X] T002 Create shared types in frontend/app/services/chatTypes.ts

---

## Phase 2: Foundational (Blocking Prerequisites)

**Purpose**: Core infrastructure that MUST be complete before ANY user story can be implemented

**⚠️ CRITICAL**: No user story work can begin until this phase is complete

- [X] T003 Add chat service wrapper for backend calls in frontend/app/services/chatApi.ts
- [X] T004 Add audio recorder utility in frontend/app/services/audioRecorder.ts
- [X] T005 Add audio playback utility in frontend/app/services/audioPlayer.ts

**Checkpoint**: Foundation ready - user story implementation can now begin

---

## Phase 3: User Story 1 - Voice Chat Session (Priority: P1) 🎯 MVP

**Goal**: Record voice input, send to backend, and display transcript with playback.

**Independent Test**: Record a prompt, see it appear in history, and play back response.

### Tests for User Story 1 (REQUIRED) ⚠️

- [X] T006 [P] [US1] Add UI state test for recording flow in frontend/tests/voiceChatRecording.test.tsx
- [X] T007 [P] [US1] Add UI state test for response playback in frontend/tests/voiceChatPlayback.test.tsx

### Implementation for User Story 1

- [X] T008 [US1] Implement voice recording toggle in frontend/app/page.tsx
- [X] T009 [US1] Implement transcript rendering in frontend/app/page.tsx
- [X] T010 [US1] Wire STT/LLM/TTS API calls in frontend/app/page.tsx
- [X] T011 [US1] Add recording indicator UI in frontend/app/components/RecordingIndicator.tsx

**Checkpoint**: User Story 1 functional and testable independently

---

## Phase 4: User Story 2 - History Navigation (Priority: P2)

**Goal**: Scrollable, chronological conversation history.

**Independent Test**: Populate multiple messages and verify scroll behavior.

### Tests for User Story 2 (REQUIRED) ⚠️

- [X] T012 [P] [US2] Add history scrolling test in frontend/tests/voiceChatHistory.test.tsx

### Implementation for User Story 2

- [X] T013 [US2] Add scrollable history container in frontend/app/page.tsx
- [X] T014 [US2] Add message grouping/styling in frontend/app/components/ChatMessage.tsx

**Checkpoint**: User Stories 1 and 2 work independently

---

## Phase 5: User Story 3 - Audio Controls (Priority: P3)

**Goal**: Explicit playback controls and retry flow.

**Independent Test**: Stop recording, see controls, replay response.

### Tests for User Story 3 (REQUIRED) ⚠️

- [X] T015 [P] [US3] Add playback control test in frontend/tests/voiceChatControls.test.tsx

### Implementation for User Story 3

- [X] T016 [US3] Add playback button UI in frontend/app/components/PlaybackControls.tsx
- [X] T017 [US3] Add retry UI and error banner in frontend/app/components/ErrorBanner.tsx

**Checkpoint**: All user stories independently functional

---

## Phase 6: Polish & Cross-Cutting Concerns

**Purpose**: Improvements that affect multiple user stories

- [X] T018 [P] Update README with UI usage in README.md
- [ ] T019 Run quickstart validation from specs/001-voice-chat-ui/quickstart.md

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
- Components before page wiring
- Story complete before moving to next priority

### Parallel Opportunities

- T006 and T007 can run in parallel
- T012 can run in parallel with other story tests once foundation is ready
- T015 can run in parallel with implementation of other stories
- T018 can run in parallel with implementation work

---

## Parallel Example: User Story 1

```bash
Task: "Add UI state test for recording flow in frontend/tests/voiceChatRecording.test.tsx"
Task: "Add UI state test for response playback in frontend/tests/voiceChatPlayback.test.tsx"
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
