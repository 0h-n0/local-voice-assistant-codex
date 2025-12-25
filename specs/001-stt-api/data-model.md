# Data Model: STT API

**Date**: 2025-12-25
**Feature**: /home/relu/misc/local-voice-assistant-codex/specs/001-stt-api/spec.md

## Entities

### TranscriptionRequest

- **id**: string (request identifier)
- **source_type**: enum (file, microphone)
- **audio_format**: enum (wav, flac, mp3)
- **duration_seconds**: integer (max 60)
- **submitted_at**: ISO-8601 timestamp

### TranscriptionResult

- **request_id**: string
- **text**: string (plain Japanese text)
- **language**: string (expected value: "ja")
- **confidence**: number (0.0 - 1.0)
- **completed_at**: ISO-8601 timestamp

### ErrorResponse

- **code**: string
- **message**: string

## Relationships

- TranscriptionResult.request_id references TranscriptionRequest.id
