# Research: Voice Orchestrator

**Date**: 2025-12-25
**Feature**: /home/relu/misc/local-voice-assistant-codex/specs/001-orchestrator/spec.md

## Decisions

- Decision: WAV-only input and output.
  Rationale: Aligns with existing STT/TTS defaults and keeps pipeline simple.
  Alternatives considered: WAV+MP3.

- Decision: Sequential STT → LLM → TTS orchestration.
  Rationale: Matches requirement and reduces complexity.
  Alternatives considered: Parallel prefetching.
