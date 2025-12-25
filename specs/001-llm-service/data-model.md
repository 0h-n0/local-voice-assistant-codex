# Data Model: LLM Service

**Date**: 2025-12-25
**Feature**: /home/relu/misc/local-voice-assistant-codex/specs/001-llm-service/spec.md

## Entities

### LlmRequest

- **id**: string (request identifier)
- **prompt**: string (max 4,000 characters)
- **submitted_at**: ISO-8601 timestamp

### LlmResponse

- **request_id**: string
- **text**: string
- **model**: string (expected: gpt-5-mini)
- **completed_at**: ISO-8601 timestamp

### ErrorResponse

- **code**: string
- **message**: string

## Relationships

- LlmResponse.request_id references LlmRequest.id
