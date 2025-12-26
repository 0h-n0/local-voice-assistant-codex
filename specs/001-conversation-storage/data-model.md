# Data Model: Conversation History Storage

## Conversation

- **id**: Client-provided identifier (unique)
- **created_at**: Timestamp when conversation first created
- **updated_at**: Timestamp of most recent message append

## Message

- **id**: Unique message identifier
- **conversation_id**: Reference to Conversation.id
- **role**: One of user, assistant, system
- **content**: Text content
- **created_at**: Timestamp when message stored

## Relationships

- Conversation 1 ── * Message (append-only)

## Validation Rules

- Conversation.id MUST be unique
- Message.role MUST be one of: user, assistant, system
- Messages are appended in creation order and never updated
