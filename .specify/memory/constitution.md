<!--
Sync Impact Report:
- Version change: 1.0.0 -> 1.1.0
- Modified principles: Added VI. Tooling and Stack Consistency
- Added sections: None
- Removed sections: None
- Templates requiring updates:
  - OK .specify/templates/plan-template.md
  - OK .specify/templates/spec-template.md
  - OK .specify/templates/tasks-template.md
  - PENDING .specify/templates/commands/*.md (directory missing)
- Follow-up TODOs: TODO(RATIFICATION_DATE) adoption date unknown
-->
# Local Voice Assistant Codex Constitution

## Core Principles

### I. Local-First Privacy and Data Minimization
User audio, transcripts, and derived data MUST remain local by default. Any network
access or external telemetry MUST require explicit, user-visible approval and be
documented in the feature spec. Logs MUST redact sensitive content unless the user
explicitly opts in to diagnostic capture.
Rationale: voice data is highly sensitive and must not leave the device without
clear consent.

### II. Deterministic, Scriptable Interfaces
All capabilities MUST be exposed through stable, scriptable interfaces with
documented inputs and outputs. When an interface is consumed by automation, it
MUST provide a machine-readable format that stays backward compatible within a
major version.
Rationale: reliable automation enables repeatable workflows and safe integration.

### III. Reliability for Critical Paths
Changes that affect intent routing, command parsing, data persistence, or device
control MUST include automated tests that cover expected success and failure
paths. Bug fixes SHOULD include regression tests unless the fix is trivial and
documented.
Rationale: critical-path regressions are costly and hard to detect manually.

### IV. Observability with User Control
Components MUST emit structured logs and error messages that make failures
actionable. Diagnostic modes MUST be opt-in, time-bounded, and respect the
privacy rules in Principle I.
Rationale: debuggability is essential without compromising privacy.

### V. Compatibility and Safe Evolution
Public commands, schemas, and configuration formats MUST follow semantic
versioning. Breaking changes MUST include migration guidance and be called out
in release notes and specs.
Rationale: stable contracts prevent downstream breakage.

### VI. Tooling and Stack Consistency
Python package management MUST use uv. Data validation for APIs and persisted
schemas MUST use Pydantic. Linting MUST be enforced with Ruff. The frontend MUST
use React/Next with TypeScript, and the backend MUST use FastAPI.
Rationale: consistent tooling and frameworks reduce integration risk and keep the
stack maintainable.

## Operational Constraints

- Default to offline operation; external services are opt-in and must degrade
  gracefully when unavailable.
- Store only the minimum data needed to fulfill the current feature scope.
- Favor deterministic processing over probabilistic behavior unless explicitly
  approved and documented.
- Use uv for Python dependency management and Ruff for linting across the repo.
- Enforce Pydantic validation for request/response schemas and stored data.

## Workflow and Quality Gates

- Each feature spec MUST document privacy impact, external dependencies, and
  any network access.
- Plans MUST include a Constitution Check confirming compliance with all core
  principles before implementation.
- Reviews MUST verify test coverage for critical paths and confirm that logging
  adheres to privacy requirements.
- Create a feature branch before implementation, update README after feature
  completion, and open a pull request for review.

## Governance

- This constitution supersedes templates and ad-hoc practices.
- Amendments require a written proposal, rationale, and updates to any impacted
  templates or guidance docs.
- Versioning policy: MAJOR for principle removals/redefinitions, MINOR for new
  principles/sections, PATCH for clarifications or wording improvements.
- Compliance review is required for every spec and plan; reviewers MUST call out
  any deviations and document approved exceptions.

**Version**: 1.1.0 | **Ratified**: TODO(RATIFICATION_DATE): adoption date unknown |
**Last Amended**: 2025-12-25
