# Data Model: Voice Orchestrator

**Date**: 2025-12-25
**Feature**: /home/relu/misc/local-voice-assistant-codex/specs/001-orchestrator/spec.md

## Entities

### OrchestratorRequest

- **id**: string (request identifier)
- **audio_bytes**: binary (WAV)
- **submitted_at**: ISO-8601 timestamp

### OrchestratorResult

- **request_id**: string
- **audio_bytes**: binary (WAV)
- **stt_text**: string
- **llm_text**: string
- **completed_at**: ISO-8601 timestamp

### StageError

- **stage**: enum (stt, llm, tts)
- **code**: string
- **message**: string

## Relationships

- OrchestratorResult.request_id references OrchestratorRequest.id
