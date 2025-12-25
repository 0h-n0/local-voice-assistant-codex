# Feature Specification: LLM Service

**Feature Branch**: `001-llm-service`  
**Created**: 2025-12-25  
**Status**: Draft  
**Input**: User description: "OpenAI の gpt-5-mini に問い合わせてテキスト応答を生成する LLM サービスを実装したい。"

## User Scenarios & Testing *(mandatory)*

### User Story 1 - Generate Text Response (Priority: P1)

As a developer, I want to send a text prompt and receive a text response so I
can integrate LLM output into applications.

**Why this priority**: Prompt-to-response is the core value of the service.

**Independent Test**: Submit a simple prompt and confirm a text response is
returned.

**Acceptance Scenarios**:

1. **Given** a valid prompt, **When** I request a response, **Then** I receive a
   text response.
2. **Given** an empty prompt, **When** I submit it, **Then** I receive a clear
   validation error.

---

### User Story 2 - Handle Provider Errors (Priority: P2)

As a developer, I want clear error responses when the upstream model fails so I
can handle failures gracefully.

**Why this priority**: Upstream failures must be visible and actionable.

**Independent Test**: Simulate a provider error and confirm the API returns a
structured error response.

**Acceptance Scenarios**:

1. **Given** the upstream provider is unavailable, **When** I send a request,
   **Then** I receive a structured error response.
2. **Given** the provider rejects the request, **When** I send it, **Then** I
   receive a structured error response indicating rejection.

---

### User Story 3 - Operational Visibility (Priority: P3)

As an operator, I want a health/status endpoint and logs so I can monitor the
service during development.

**Why this priority**: Operational visibility speeds diagnosis.

**Independent Test**: Call the health endpoint and confirm a ready response.

**Acceptance Scenarios**:

1. **Given** the service is running, **When** I check health status, **Then** I
   receive a ready response.
2. **Given** an invalid request, **When** I submit it, **Then** logs capture the
   failure without exposing prompt content.

---

### Edge Cases

- What happens when the prompt exceeds the service limit?
- How does the service respond to upstream timeouts?
- What happens when credentials are missing or invalid?

## Clarifications

### Session 2025-12-25

- Q: Should prompts/responses be persisted? → A: Do not persist prompts/responses
- Q: Should the LLM responses be streamed or single response? → A: Non-streaming (single response)

## Requirements *(mandatory)*

### Functional Requirements

- **FR-001**: The service MUST accept a text prompt and return a text response.
- **FR-008**: The service MUST return a single, non-streaming response.
- **FR-002**: The service MUST send prompts to OpenAI gpt-5-mini and return the
  resulting response text.
- **FR-003**: The service MUST validate prompts and reject empty input with a
  clear error response.
- **FR-004**: The service MUST provide structured error responses for upstream
  failures.
- **FR-005**: The service MUST expose a health/status endpoint for readiness
  checks.

*Example of marking unclear requirements:*

- **FR-006**: The service MUST enforce a maximum prompt length of 4,000 characters.
- **FR-007**: The service MUST not persist prompts or responses beyond request processing.

### Technical Constraints *(mandatory)*

- **TC-001**: Frontend MUST use React/Next with TypeScript.
- **TC-002**: Backend MUST use FastAPI.
- **TC-003**: Python dependency management MUST use uv.
- **TC-004**: Data validation MUST use Pydantic schemas.
- **TC-005**: Linting MUST be enforced with Ruff.

### Key Entities *(include if feature involves data)*

- **LlmRequest**: Prompt text and request metadata.
- **LlmResponse**: Response text and usage metadata.
- **ErrorResponse**: Error code and human-readable message.

### Assumptions and Dependencies

- Operators provide valid OpenAI credentials via secure configuration.
- Network access is permitted for outbound model requests.

## Success Criteria *(mandatory)*

### Measurable Outcomes

- **SC-001**: 95% of valid prompts return a text response.
- **SC-002**: Responses for short prompts are returned within 5 seconds under
  typical load.
- **SC-003**: 100% of invalid inputs return structured error responses.
- **SC-004**: Developers can complete a basic integration within 30 minutes
  using provided API documentation.
