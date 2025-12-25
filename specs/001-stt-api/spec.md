# Feature Specification: STT API

**Feature Branch**: `001-stt-api`  
**Created**: 2025-12-25  
**Status**: Draft  
**Input**: User description: "reazon-research/reazonspeech-nemo-v2 を用いて音声ファイルまたはマイク入力から日本語テキストを生成する STT API を実装したい。"

## User Scenarios & Testing *(mandatory)*

### User Story 1 - Transcribe Audio File (Priority: P1)

As a developer, I want to submit a Japanese audio file and receive transcribed
text so I can integrate speech-to-text into applications.

**Why this priority**: File transcription is the core API value and the simplest
entry point for adopters.

**Independent Test**: Submit a known Japanese audio sample and verify the API
returns text output.

**Acceptance Scenarios**:

1. **Given** a valid Japanese audio file, **When** I submit it for transcription,
   **Then** I receive a text response.
2. **Given** a non-audio file, **When** I submit it, **Then** I receive a clear
   error response.

---

### User Story 2 - Transcribe Microphone Input (Priority: P2)

As a developer, I want to stream microphone input to the API and receive
transcribed Japanese text so I can support live transcription workflows.

**Why this priority**: Live input enables real-time use cases beyond batch
transcription.

**Independent Test**: Send a short microphone recording and verify a text
response is returned.

**Acceptance Scenarios**:

1. **Given** a microphone input stream, **When** I send audio frames,
   **Then** I receive transcribed text output.
2. **Given** the stream stops, **When** I finalize the request, **Then** I
   receive the final transcription.

---

### User Story 3 - Operational Visibility (Priority: P3)

As an operator, I want clear error reporting and status information so I can
monitor the STT API during development.

**Why this priority**: Operational clarity reduces debugging time and supports
reliable usage.

**Independent Test**: Trigger a failure and confirm the API returns a clear error
code and message.

**Acceptance Scenarios**:

1. **Given** an unsupported audio format, **When** I submit it, **Then** I
   receive a structured error response.
2. **Given** the service is running, **When** I check health status, **Then** I
   receive a ready response.

---

### Edge Cases

- What happens when audio duration exceeds the service limit?
- How does the API respond to silence-only audio?
- What happens when the model is not loaded or initialization fails?

## Clarifications

### Session 2025-12-25

- Q: Which audio formats are supported for file uploads? → A: WAV, FLAC, MP3
- Q: Should the API require authentication? → A: No authentication
- Q: What input protocol should be used for microphone streaming? → A: WebSocket streaming

## Requirements *(mandatory)*

### Functional Requirements

- **FR-001**: The API MUST accept Japanese audio files and return transcribed
  text in the response.
- **FR-002**: The API MUST support microphone input transcription via a WebSocket
  streaming request.
- **FR-003**: The API MUST validate input audio format and return clear errors
  for unsupported formats.
- **FR-009**: The API MUST accept WAV, FLAC, and MP3 uploads.
- **FR-004**: The API MUST expose a health/status endpoint for readiness checks.
- **FR-005**: The API MUST provide structured error responses for failures.

*Example of marking unclear requirements:*

- **FR-006**: The API MUST enforce an audio length limit of 60 seconds per
  request.
- **FR-007**: The API MUST return transcription as plain text.
- **FR-008**: The API MUST not require authentication.

### Technical Constraints *(mandatory)*

- **TC-001**: Frontend MUST use React/Next with TypeScript.
- **TC-002**: Backend MUST use FastAPI.
- **TC-003**: Python dependency management MUST use uv.
- **TC-004**: Data validation MUST use Pydantic schemas.
- **TC-005**: Linting MUST be enforced with Ruff.

### Key Entities *(include if feature involves data)*

- **TranscriptionRequest**: Audio payload, source type (file or microphone), and
  request metadata.
- **TranscriptionResult**: Transcribed text, language, and confidence metadata.
- **ErrorResponse**: Error code and human-readable message.

### Assumptions and Dependencies

- Requests remain within the documented audio length limit.
- Clients can provide audio in supported formats and network connectivity for
  API calls.

## Success Criteria *(mandatory)*

### Measurable Outcomes

- **SC-001**: 95% of valid audio requests return a transcription response.
- **SC-002**: Users can obtain a transcription within 10 seconds for a 10-second
  audio sample under typical load.
- **SC-003**: 100% of invalid inputs return a structured error response.
- **SC-004**: Developers can complete a basic integration within 30 minutes using
  provided API documentation.
