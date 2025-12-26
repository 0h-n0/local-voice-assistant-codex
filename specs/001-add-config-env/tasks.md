# Task Plan: Config Source Management

**Feature**: Config Source Management
**Branch**: `001-add-config-env`
**Plan**: /home/relu/misc/local-voice-assistant-codex/specs/001-add-config-env/plan.md

## Phase 1: Setup

**Goal**: Establish configuration scaffolding and documentation updates.
**Independent Test Criteria**: Configuration module loads with defaults and documentation updated.

- [X] T001 Create config directory structure in backend/app/config/ for config loaders
- [X] T002 Add sample config template at backend/app/config/config.sample.toml
- [X] T003 Update README to document config sources and precedence in README.md

## Phase 2: Foundational

**Goal**: Implement core config loading, validation, and redaction utilities.
**Independent Test Criteria**: Config values resolve correctly across sources with redaction applied.

- [X] T004 Implement Pydantic settings model in backend/app/config/settings.py
- [X] T005 Implement TOML config file loader in backend/app/config/file_loader.py
- [X] T006 Implement precedence resolver in backend/app/config/resolver.py
- [X] T007 Implement redaction utilities in backend/app/config/redaction.py
- [X] T008 Update backend/app/config.py to use new settings resolver

## Phase 3: User Story 1 (P1) - Centralized Configuration

**Story Goal**: Operators can load configuration from .env, env vars, and config file.
**Independent Test Criteria**: Config resolves as env > .env > config file with correct values.

- [X] T009 [US1] Add .env loading integration in backend/app/config/settings.py
- [X] T010 [US1] Add env-var mapping for API keys, model paths, audio device settings in backend/app/config/settings.py
- [X] T011 [US1] Add unit tests for precedence rules in backend/tests/test_config_precedence.py

## Phase 4: User Story 2 (P2) - Safe Validation and Feedback

**Story Goal**: Invalid configuration is rejected with actionable errors.
**Independent Test Criteria**: Missing/invalid values return field-specific errors.

- [X] T012 [US2] Implement validation error formatting in backend/app/config/resolver.py
- [X] T013 [US2] Add unit tests for validation errors in backend/tests/test_config_validation.py

## Phase 5: User Story 3 (P3) - Configuration Visibility

**Story Goal**: Operators can view redacted effective configuration.
**Independent Test Criteria**: Config summary endpoint returns redacted values for sensitive fields.

- [X] T014 [US3] Add config summary schema in backend/app/schemas/config_summary.py
- [X] T015 [US3] Implement config summary endpoint in backend/app/api/config.py
- [X] T016 [US3] Wire config summary route into backend/app/main.py
- [X] T017 [US3] Add endpoint tests in backend/tests/test_config_summary.py

## Phase 6: Polish & Cross-Cutting Concerns

**Goal**: Ensure documentation and tooling compliance.
**Independent Test Criteria**: Docs updated, lint/test instructions verified.

- [X] T018 Add quickstart updates to specs/001-add-config-env/quickstart.md
- [X] T019 Verify Ruff configuration references new config files in backend/pyproject.toml

## Dependencies

- US1 blocks US2 and US3.
- US2 and US3 can run in parallel after US1 completes.

## Parallel Execution Examples

- US2 and US3 tasks can be executed in parallel once configuration loading is implemented.
- Tests for US2 and US3 can be run in parallel if they touch different files.

## Implementation Strategy

- Start with config model + resolver utilities (Phase 2).
- Implement US1 end-to-end with precedence rules.
- Add validation/error handling (US2) and summary endpoint (US3).
- Finish with docs and lint verification.
