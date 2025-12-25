# Research: STT API

**Date**: 2025-12-25
**Feature**: /home/relu/misc/local-voice-assistant-codex/specs/001-stt-api/spec.md

## Decisions

- Decision: Use reazon-research/reazonspeech-nemo-v2 for Japanese STT.
  Rationale: Explicitly requested model and Japanese transcription support.
  Alternatives considered: Whisper, NeMo ASR baselines.

- Decision: WebSocket streaming for microphone input.
  Rationale: Lower latency and clearer streaming semantics than chunked uploads.
  Alternatives considered: Chunked HTTP uploads.

- Decision: Support WAV, FLAC, and MP3 file uploads.
  Rationale: Common audio formats with strong tooling support.
  Alternatives considered: WAV-only.

- Decision: Limit audio duration to 60 seconds per request.
  Rationale: Keeps latency and compute bounded for local use.
  Alternatives considered: 30s, 300s.
