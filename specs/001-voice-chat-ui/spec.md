# Feature Specification: Voice Chat Web UI

**Feature Branch**: `001-voice-chat-ui`  
**Created**: 2025-12-27  
**Status**: Draft  
**Input**: User description: "ChatGPTのように会話履歴が表示され、音声入力と音声出力ができるWeb UIを実装したい。"

## Clarifications

### Session 2025-12-27

- Q: What recording interaction should the UI use? → A: Toggle (click to start/stop).
- Q: Should audio replies auto-play or require user action? → A: Require explicit user action.
- Q: Should the UI support multiple conversations or a single active conversation? → A: Single active conversation.
- Q: How should transcription be displayed during recording? → A: Show recording indicator only; transcribe after stop.
- Q: Should conversation history persist across reloads? → A: In-memory only; clear on reload.
- Q: How should recording/playback errors be surfaced? → A: Minimal errors banner + inline message.

## User Scenarios & Testing *(mandatory)*

### User Story 1 - Voice Chat Session (Priority: P1)

As a user, I want to speak to the assistant and see the conversation history so I can
conduct a continuous voice-based chat.

**Why this priority**: Voice interaction with visible history is the core experience.

**Independent Test**: Record a voice prompt, receive a spoken reply, and verify both
messages appear in the history.

**Acceptance Scenarios**:

1. **Given** the chat page is open, **When** the user records a voice prompt,
   **Then** the prompt appears in the conversation history.
2. **Given** a stored assistant response, **When** playback is triggered,
   **Then** audio output plays and the response is visible in the history.

---

### User Story 2 - History Navigation (Priority: P2)

As a user, I want to scroll through prior messages so I can review the conversation.

**Why this priority**: History review is essential for context in longer sessions.

**Independent Test**: Populate a conversation with multiple turns and verify scrolling
and message grouping work as expected.

**Acceptance Scenarios**:

1. **Given** a long conversation, **When** the user scrolls upward,
   **Then** earlier messages remain readable and ordered.

---

### User Story 3 - Audio Controls (Priority: P3)

As a user, I want to control recording and playback so I can manage voice interaction.

**Why this priority**: Controls provide reliable interaction for varied environments.

**Independent Test**: Start and stop recording and replay the latest response.

**Acceptance Scenarios**:

1. **Given** the chat page is open, **When** the user stops recording,
   **Then** the UI indicates recording ended and the message is queued for reply.

---

### Edge Cases

- What happens when the microphone permission is denied?
- How does the UI behave when audio output is unavailable?

## Requirements *(mandatory)*

### Functional Requirements

- **FR-001**: System MUST display a chronological conversation history.
- **FR-002**: Users MUST be able to record voice prompts in the UI.
- **FR-003**: System MUST play back assistant responses as audio output.
- **FR-004**: System MUST show recording status and playback status.
- **FR-005**: System MUST allow users to retry after a failed recording.
- **FR-006**: Recording MUST be controlled via a start/stop toggle interaction.
- **FR-007**: Audio playback MUST require explicit user action.
- **FR-008**: UI MUST focus on a single active conversation view.
- **FR-009**: During recording, UI MUST show only a recording indicator and render text after stop.
- **FR-010**: Conversation history MUST clear on page reload.
- **FR-011**: UI MUST display errors via a minimal banner and inline message.

### Technical Constraints *(mandatory)*

- **TC-001**: Frontend MUST use React/Next with TypeScript.
- **TC-002**: Backend MUST use FastAPI.
- **TC-003**: Python dependency management MUST use uv.
- **TC-004**: Data validation MUST use Pydantic schemas.
- **TC-005**: Linting MUST be enforced with Ruff.

### Assumptions

- The UI runs in a modern desktop browser with microphone support.
- Voice input/output remains local and does not require third-party services.

### Key Entities *(include if feature involves data)*

- **ChatMessage**: Represents a single user or assistant message in the UI.
- **AudioClip**: Represents recorded input or synthesized output audio.

## Success Criteria *(mandatory)*

### Measurable Outcomes

- **SC-001**: Users can complete a voice prompt and receive a reply in under 10 seconds.
- **SC-002**: 90% of sessions show correct message ordering in the history.
- **SC-003**: 95% of users successfully start and stop recording on first attempt.
- **SC-004**: Audio playback succeeds without manual retry in 95% of interactions.
