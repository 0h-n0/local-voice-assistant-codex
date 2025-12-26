# Feature Specification: Config Source Management

**Feature Branch**: `001-add-config-env`  
**Created**: 2025-09-28  
**Status**: Draft  
**Input**: User description: "APIキー、モデルパス、音声デバイスなどを設定ファイルまたは .env で管理できるようにしたい。"

## Clarifications

### Session 2025-09-28

- Q: Which configuration sources should be supported? → A: .env, environment variables, and a single config file.
- Q: What precedence order should apply across sources? → A: Environment variables > .env > config file.
- Q: How should sensitive values be shown in configuration summaries? → A: Redact with a fixed mask (e.g., ****).

## User Scenarios & Testing *(mandatory)*

### User Story 1 - Centralized Configuration (Priority: P1)

As an operator, I want to set API keys, model paths, and audio device settings from
configuration sources so I can change runtime behavior without code edits.

**Why this priority**: This unlocks safe, repeatable deployments and is required for any
non-trivial environment setup.

**Independent Test**: Provide configuration values through supported sources and confirm
the system picks them up consistently across startup and runtime checks.

**Acceptance Scenarios**:

1. **Given** configuration values are provided via .env, environment variables, or a
   config file, **When** the system starts,
   **Then** the effective configuration matches the provided values.
2. **Given** a value is provided in multiple sources, **When** the system starts,
   **Then** the documented precedence rules determine the effective value.

---

### User Story 2 - Safe Validation and Feedback (Priority: P2)

As an operator, I want invalid configuration values to be rejected with clear feedback
so I can correct mistakes quickly.

**Why this priority**: Misconfiguration is the most common failure mode and needs to be
actionable.

**Independent Test**: Supply invalid values and confirm the system reports validation
errors with the field name and reason.

**Acceptance Scenarios**:

1. **Given** a required value is missing, **When** configuration is validated,
   **Then** the system reports the missing field and expected format.
2. **Given** a value fails validation rules, **When** configuration is validated,
   **Then** the system reports the field and reason without crashing.

---

### User Story 3 - Configuration Visibility (Priority: P3)

As an operator, I want to inspect the effective configuration (excluding secrets) so I
can confirm the system is using the intended settings.

**Why this priority**: Visibility reduces troubleshooting time and prevents accidental
misconfiguration.

**Independent Test**: Request a configuration summary and verify it includes all
non-sensitive settings and hides secrets.

**Acceptance Scenarios**:

1. **Given** configuration values are loaded, **When** a configuration summary is
   requested, **Then** it lists effective values for non-sensitive fields.
2. **Given** a field is marked sensitive, **When** the configuration summary is
   requested, **Then** the sensitive value is masked or omitted.

---

### Edge Cases

- What happens when configuration sources disagree on a required value?
- How does system handle a configuration file that is unreadable or malformed?

## Requirements *(mandatory)*

### Functional Requirements

- **FR-001**: System MUST load configuration from at least one supported source.
- **FR-001a**: System MUST support .env, environment variables, and a single config
  file as configuration sources.
- **FR-002**: System MUST define and apply deterministic precedence rules across sources.
- **FR-002a**: System MUST apply precedence as: environment variables > .env > config
  file.
- **FR-003**: System MUST validate configuration values at startup and before use.
- **FR-004**: System MUST provide actionable validation errors with field name and reason.
- **FR-005**: System MUST prevent sensitive values from being exposed in summaries.
- **FR-005a**: System MUST redact sensitive values using a fixed mask in summaries.
- **FR-006**: System MUST allow operators to view the effective non-sensitive
  configuration values.

### Technical Constraints *(mandatory)*

- **TC-001**: Frontend MUST use React/Next with TypeScript.
- **TC-002**: Backend MUST use FastAPI.
- **TC-003**: Python dependency management MUST use uv.
- **TC-004**: Data validation MUST use Pydantic schemas.
- **TC-005**: Linting MUST be enforced with Ruff.

### Key Entities *(include if feature involves data)*

- **Configuration Setting**: A named setting with a value, source, and sensitivity flag.
- **Effective Configuration**: The resolved set of settings after applying precedence.

## Success Criteria *(mandatory)*

### Measurable Outcomes

- **SC-001**: 95% of configuration changes are applied successfully on the first attempt.
- **SC-002**: Configuration validation completes within 5 seconds for typical setups.
- **SC-003**: Operators can confirm effective non-sensitive settings within 1 minute.
- **SC-004**: 100% of invalid configurations return a field-specific error message.
