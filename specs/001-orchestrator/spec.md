# Feature Specification: Voice Orchestrator

**Feature Branch**: `001-orchestrator`  
**Created**: 2025-12-25  
**Status**: Draft  
**Input**: User description: "STT → LLM → TTS を順番に実行し、1つの音声対話を完結させるオーケストレーターを実装したい。"

## User Scenarios & Testing *(mandatory)*

### User Story 1 - End-to-End Voice Flow (Priority: P1)

As a developer, I want to submit an audio input and receive synthesized speech
so I can complete a single conversational turn end-to-end.

**Why this priority**: End-to-end orchestration is the core value of the feature.

**Independent Test**: Submit a short audio sample and receive a synthesized
response audio file.

**Acceptance Scenarios**:

1. **Given** a valid audio input, **When** I run the orchestrator, **Then** I
   receive a synthesized audio response.
2. **Given** missing input audio, **When** I run the orchestrator, **Then** I
   receive a clear validation error.

---

### User Story 2 - Orchestration Error Handling (Priority: P2)

As a developer, I want the orchestrator to surface clear errors from STT, LLM,
and TTS so I can diagnose failures.

**Why this priority**: Transparent failures reduce debugging time and improve
stability.

**Independent Test**: Simulate a failure in each stage and confirm a structured
error response.

**Acceptance Scenarios**:

1. **Given** the STT stage fails, **When** I run the orchestrator, **Then** I
   receive a structured error response indicating STT failure.
2. **Given** the LLM stage fails, **When** I run the orchestrator, **Then** I
   receive a structured error response indicating LLM failure.

---

### User Story 3 - Operational Visibility (Priority: P3)

As an operator, I want a health/status endpoint so I can monitor the
orchestrator service during development.

**Why this priority**: Operational visibility speeds diagnosis.

**Independent Test**: Call the health endpoint and confirm a ready response.

**Acceptance Scenarios**:

1. **Given** the service is running, **When** I check health status, **Then** I
   receive a ready response.
2. **Given** a failure occurs, **When** I inspect logs, **Then** I can identify
   which stage failed without exposing audio content.

---

### Edge Cases

- What happens when STT returns empty text?
- How does the orchestrator handle timeouts in any stage?
- What happens when TTS returns an invalid audio payload?

## Clarifications

### Session 2025-12-25

- Q: What audio output format should be returned? → A: WAV only
- Q: What audio input format should be supported? → A: WAV only

## Requirements *(mandatory)*

### Functional Requirements

- **FR-001**: The orchestrator MUST accept an audio input and return synthesized
  audio output.
- **FR-002**: The orchestrator MUST run STT → LLM → TTS in sequence.
- **FR-003**: The orchestrator MUST return structured errors when any stage
  fails.
- **FR-004**: The orchestrator MUST expose a health/status endpoint for
  readiness checks.

*Example of marking unclear requirements:*

- **FR-005**: The orchestrator MUST accept audio input in WAV format.
- **FR-006**: The orchestrator MUST return audio output in WAV format.

### Technical Constraints *(mandatory)*

- **TC-001**: Frontend MUST use React/Next with TypeScript.
- **TC-002**: Backend MUST use FastAPI.
- **TC-003**: Python dependency management MUST use uv.
- **TC-004**: Data validation MUST use Pydantic schemas.
- **TC-005**: Linting MUST be enforced with Ruff.

### Key Entities *(include if feature involves data)*

- **OrchestratorRequest**: Audio input and request metadata.
- **OrchestratorResult**: Synthesized audio output and stage metadata.
- **StageError**: Error code, stage identifier, and human-readable message.

### Assumptions and Dependencies

- STT, LLM, and TTS services are available locally.
- Orchestrator can call each service without network restrictions.

## Success Criteria *(mandatory)*

### Measurable Outcomes

- **SC-001**: 95% of valid inputs return synthesized audio successfully.
- **SC-002**: End-to-end orchestration completes within 15 seconds for a
  short input under typical load.
- **SC-003**: 100% of stage failures return structured error responses.
- **SC-004**: Developers can integrate the orchestrator within 30 minutes using
  provided documentation.
