# Feature Specification: Realtime Voice WebSocket

**Feature Branch**: `001-realtime-ws`  
**Created**: 2025-12-27  
**Status**: Draft  
**Input**: User description: "音声入力・文字起こし・応答・音声再生をリアルタイムで表示できるように WebSocket 通信を追加したい。"

## Clarifications

### Session 2025-12-27

- Q: What should be sent over WebSocket? → A: Text + audio events (binary frames).
- Q: How should the WebSocket authenticate? → A: Token in Sec-WebSocket-Protocol.
- Q: What event types should the stream emit? → A: status, transcript, response, audio.
- Q: Should transcripts be partial or final only? → A: Partial transcripts + final transcript.
- Q: How should reconnects be handled? → A: Auto-reconnect without resume.
- Q: What audio framing should be used? → A: WAV chunks, 100–200ms.

## User Scenarios & Testing *(mandatory)*

### User Story 1 - Live Voice Stream (Priority: P1)

As a user, I want to see live transcription and response updates while speaking so
I can follow the conversation in real time.

**Why this priority**: Real-time feedback is the core value of WebSocket streaming.

**Independent Test**: Stream audio frames and verify partial transcription events
and a final response event are displayed live.

**Acceptance Scenarios**:

1. **Given** a WebSocket connection is open, **When** audio frames arrive,
   **Then** partial transcription updates are emitted to the UI.
2. **Given** the stream ends, **When** processing completes,
   **Then** the final response and audio playback event are emitted.

---

### User Story 2 - Live Response Playback (Priority: P2)

As a user, I want audio output to start once the response is ready so I can hear it
without waiting for a full refresh.

**Why this priority**: Immediate response playback reinforces the real-time experience.

**Independent Test**: Receive a response event and confirm playback triggers once.

**Acceptance Scenarios**:

1. **Given** a response event arrives, **When** the UI receives audio data,
   **Then** playback starts after explicit user action.

---

### User Story 3 - Stream Status Feedback (Priority: P3)

As a user, I want clear status indicators during streaming so I know what is
happening in real time.

**Why this priority**: Real-time flows need transparency for trust.

**Independent Test**: Trigger each stream state and confirm the UI updates accordingly.

**Acceptance Scenarios**:

1. **Given** streaming starts, **When** status updates are sent,
   **Then** the UI shows recording, transcribing, and responding states.

---

### Edge Cases

- What happens when the WebSocket connection drops mid-stream?
- How does the UI handle a stream that ends with no audio frames?

## Requirements *(mandatory)*

### Functional Requirements

- **FR-001**: System MUST accept audio frames over WebSocket and emit partial transcription updates.
- **FR-002**: System MUST emit a final response event when processing completes.
- **FR-003**: UI MUST display real-time transcription updates as they arrive.
- **FR-004**: UI MUST display stream status changes (recording, transcribing, responding).
- **FR-005**: UI MUST trigger audio playback only after explicit user action.
- **FR-006**: System MUST send text events and audio frames over the WebSocket stream.
- **FR-007**: WebSocket connections MUST support auth token via Sec-WebSocket-Protocol.
- **FR-008**: Stream MUST emit events: status, transcript, response, audio.
- **FR-009**: Stream MUST emit partial transcript updates and a final transcript.
- **FR-010**: Client MUST auto-reconnect and restart the stream on disconnect.
- **FR-011**: Audio frames MUST be WAV chunks in 100–200ms slices.

### Technical Constraints *(mandatory)*

- **TC-001**: Frontend MUST use React/Next with TypeScript.
- **TC-002**: Backend MUST use FastAPI.
- **TC-003**: Python dependency management MUST use uv.
- **TC-004**: Data validation MUST use Pydantic schemas.
- **TC-005**: Linting MUST be enforced with Ruff.

### Assumptions

- Audio frames are encoded as WAV chunks compatible with backend processing.
- WebSocket communication remains local and does not require external services.

### Key Entities *(include if feature involves data)*

- **StreamEvent**: Represents a single WebSocket event in the stream.
- **StreamState**: Represents the current UI status of the stream.

## Success Criteria *(mandatory)*

### Measurable Outcomes

- **SC-001**: Partial transcription updates appear within 1 second of receiving frames.
- **SC-002**: Final response arrives within 5 seconds after stream end for a 10s clip.
- **SC-003**: 95% of sessions successfully complete without dropped WebSocket connection.
- **SC-004**: 90% of users report the stream status indicators are clear.
