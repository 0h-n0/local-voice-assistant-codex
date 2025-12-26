# Feature Specification: Conversation History Storage

**Feature Branch**: `001-conversation-storage`  
**Created**: 2025-12-26  
**Status**: Draft  
**Input**: User description: "ユーザーとアシスタントの会話履歴を保存・取得できるストレージ機能を実装したい。SQLiteを想定。"

## Clarifications

### Session 2025-12-26

- Q: Which roles should be stored for conversation messages? → A: Store user, assistant, and system roles.
- Q: How should conversation IDs be assigned? → A: Client provides the conversation ID.
- Q: Should messages be append-only or editable? → A: Append-only.
- Q: If a conversation ID already exists, how should new messages be handled? → A: Append messages to the existing conversation.

## User Scenarios & Testing *(mandatory)*

### User Story 1 - Save Conversation Messages (Priority: P1)

As a user, I want my conversation messages to be stored so I can retrieve them later.

**Why this priority**: Persistent storage is the core value of conversation history.

**Independent Test**: Save a conversation with multiple messages and retrieve it to verify
all messages are returned in the original order.

**Acceptance Scenarios**:

1. **Given** a new conversation, **When** the user submits messages, **Then** the
   system stores each message with its role and timestamp.
2. **Given** a stored conversation, **When** the user requests its history, **Then**
   the system returns all messages in the correct sequence.

---

### User Story 2 - List Conversations (Priority: P2)

As a user, I want to see a list of my past conversations so I can reopen one.

**Why this priority**: Listing makes stored histories discoverable and usable.

**Independent Test**: Create multiple conversations and verify the list returns each
conversation summary once.

**Acceptance Scenarios**:

1. **Given** multiple stored conversations, **When** the user requests the list,
   **Then** the system returns summaries with identifiers and last-updated times.

---

### User Story 3 - Remove Conversations (Priority: P3)

As a user, I want to delete a conversation I no longer need.

**Why this priority**: Users need control over their stored history.

**Independent Test**: Create a conversation, delete it, and confirm it no longer appears
in lists or retrieval.

**Acceptance Scenarios**:

1. **Given** a stored conversation, **When** the user deletes it, **Then** the
   system removes it from storage and subsequent retrieval fails gracefully.

---

### Edge Cases

- What happens when a conversation has zero messages?
- How does the system handle requests for a non-existent conversation ID?

## Requirements *(mandatory)*

### Functional Requirements

- **FR-001**: System MUST store conversation messages with role, content, and timestamp.
- **FR-006**: System MUST support message roles: user, assistant, and system.
- **FR-002**: System MUST return all messages for a conversation in creation order.
- **FR-003**: Users MUST be able to list conversation summaries with identifiers.
- **FR-004**: Users MUST be able to delete a conversation and all its messages.
- **FR-005**: System MUST return a clear not-found response for unknown conversation IDs.
- **FR-007**: System MUST accept a client-provided conversation ID when saving messages.
- **FR-008**: System MUST treat conversation messages as append-only (no edits).
- **FR-009**: System MUST append new messages to an existing conversation ID.

### Technical Constraints *(mandatory)*

- **TC-001**: Frontend MUST use React/Next with TypeScript.
- **TC-002**: Backend MUST use FastAPI.
- **TC-003**: Python dependency management MUST use uv.
- **TC-004**: Data validation MUST use Pydantic schemas.
- **TC-005**: Linting MUST be enforced with Ruff.
- **TC-006**: Persistent storage MUST use SQLite.

### Assumptions

- The system is used in a single-tenant local environment.
- Authentication and authorization are handled by another component.
- Conversation history is retained until a user deletes it.

### Key Entities *(include if feature involves data)*

- **Conversation**: Represents one dialog session, with identifier and timestamps.
- **Message**: Represents a single user or assistant message tied to a conversation.

## Success Criteria *(mandatory)*

### Measurable Outcomes

- **SC-001**: 95% of users can retrieve a saved conversation on the first attempt.
- **SC-002**: Users can save a 20-message conversation in under 5 seconds.
- **SC-003**: Listing conversations returns results in under 2 seconds for 100 entries.
- **SC-004**: 90% of deletion attempts remove a conversation without follow-up errors.
