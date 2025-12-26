# Data Model: Voice Chat Web UI

## ChatMessage

- **id**: Unique identifier
- **role**: user or assistant
- **content**: Text content
- **created_at**: Timestamp

## AudioClip

- **id**: Unique identifier
- **kind**: input (recorded) or output (synthesized)
- **duration_ms**: Length of audio clip
- **created_at**: Timestamp

## Relationships

- ChatMessage may reference an AudioClip (input or output)
