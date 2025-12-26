# Data Model: TTS API

**Date**: 2025-12-25
**Feature**: /home/relu/misc/local-voice-assistant-codex/specs/001-tts-api/spec.md

## Entities

### TtsRequest

- **id**: string (request identifier)
- **text**: string (max 1,000 characters)
- **voice**: string (voice/style identifier)
- **submitted_at**: ISO-8601 timestamp

### TtsResponse

- **request_id**: string
- **audio_format**: string (wav)
- **audio_bytes**: binary
- **completed_at**: ISO-8601 timestamp

### ErrorResponse

- **code**: string
- **message**: string

## Relationships

- TtsResponse.request_id references TtsRequest.id
