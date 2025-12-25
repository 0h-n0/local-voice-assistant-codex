# Research: LLM Service

**Date**: 2025-12-25
**Feature**: /home/relu/misc/local-voice-assistant-codex/specs/001-llm-service/spec.md

## Decisions

- Decision: Use OpenAI gpt-5-mini for prompt completion.
  Rationale: Explicitly requested provider/model.
  Alternatives considered: Other OpenAI models.

- Decision: Non-streaming responses.
  Rationale: Simplifies integration and aligns with clarified requirement.
  Alternatives considered: Streaming responses.

- Decision: 4,000 character prompt limit.
  Rationale: Keeps requests bounded and predictable.
  Alternatives considered: 1,000, 8,000.

- Decision: Do not persist prompts or responses.
  Rationale: Aligns with privacy constraints and reduces risk.
  Alternatives considered: Short-term logging.
