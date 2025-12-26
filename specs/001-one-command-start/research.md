# Research: One-Command Service Startup

## Decision 1: Startup tooling

**Decision**: Provide docker-compose as the primary orchestrator and a Makefile wrapper
for start/stop/status convenience.

**Rationale**: docker-compose is standard for local multi-service orchestration, while
Makefile offers a single entry point and consistent CLI UX.

**Alternatives considered**:
- Makefile only (less standardized for multi-container environments)
- Shell scripts only (less discoverable and harder to extend)

## Decision 2: Default service set

**Decision**: Default services are backend and frontend, plus any required runtime
services declared in docker-compose (e.g., database if needed).

**Rationale**: Keeps the default list minimal and aligned with the feature scope while
allowing docker-compose to define supporting dependencies.

**Alternatives considered**:
- Auto-detect running processes (unreliable and inconsistent)
- Require explicit service list in config (adds operator burden)

## Decision 3: Idempotent behavior

**Decision**: Start/stop commands should be safe to re-run; docker-compose handles
idempotency via container state checks.

**Rationale**: Reduces operator risk and prevents duplicate processes.

**Alternatives considered**:
- Hard stop on already-running services (adds friction without benefit)
