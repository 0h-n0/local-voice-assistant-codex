# Research: Conversation History Storage

## Decision 1: Conversation ID assignment

**Decision**: Client provides conversation IDs.
**Rationale**: Supports retries and external correlation without server-side state.
**Alternatives considered**: Server-generated IDs; mixed mode.

## Decision 2: Message mutability

**Decision**: Append-only messages.
**Rationale**: Preserves history integrity and simplifies auditability.
**Alternatives considered**: Editable messages with update semantics.

## Decision 3: Message roles

**Decision**: Store user, assistant, and system roles.
**Rationale**: Supports future system prompts and aligns with LLM usage patterns.
**Alternatives considered**: User/assistant only.

## Decision 4: Existing ID behavior

**Decision**: Append new messages to existing conversation IDs.
**Rationale**: Maintains continuity and aligns with append-only requirement.
**Alternatives considered**: Reject on conflict; overwrite existing history.
