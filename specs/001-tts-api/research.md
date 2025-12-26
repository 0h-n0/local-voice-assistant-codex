# Research: TTS API

**Date**: 2025-12-25
**Feature**: /home/relu/misc/local-voice-assistant-codex/specs/001-tts-api/spec.md

## Decisions

- Decision: Use Style-Bert-VITS2 for Japanese TTS.
  Rationale: Explicitly requested model.
  Alternatives considered: Other TTS models.

- Decision: WAV output format.
  Rationale: Most compatible and simple for TTS output.
  Alternatives considered: MP3, WAV+MP3.

- Decision: 1,000 character max text length.
  Rationale: Bounds compute and latency.
  Alternatives considered: 2,000, 5,000.
