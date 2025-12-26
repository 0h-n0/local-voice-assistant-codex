# Task Plan: One-Command Service Startup

**Feature**: One-Command Service Startup
**Branch**: `001-one-command-start`
**Plan**: /home/relu/misc/local-voice-assistant-codex/specs/001-one-command-start/plan.md

## Phase 1: Setup

**Goal**: Establish orchestration files and baseline docs.
**Independent Test Criteria**: Orchestration files exist and README lists startup commands.

- [X] T001 Create docker-compose.yml with backend and frontend services
- [X] T002 Create Makefile with start/stop/status targets
- [X] T003 Update README with one-command startup instructions in README.md

## Phase 2: Foundational

**Goal**: Define defaults, health checks, and idempotent behavior.
**Independent Test Criteria**: Compose services start with health checks and
commands are idempotent.

- [X] T004 Define default service list and health checks in docker-compose.yml
- [X] T005 Implement idempotent start/stop in Makefile targets
- [X] T006 Add status output formatting in Makefile status target

## Phase 3: User Story 1 (P1) - Start All Services

**Story Goal**: Operators can start all services with a single command.
**Independent Test Criteria**: `make start` brings backend and frontend up and
ports respond.

- [X] T007 [US1] Add backend container configuration in docker-compose.yml
- [X] T008 [US1] Add frontend container configuration in docker-compose.yml
- [X] T009 [US1] Document default service set in README.md

## Phase 4: User Story 2 (P2) - Stop and Cleanup

**Story Goal**: Operators can stop services with a single command.
**Independent Test Criteria**: `make stop` stops all containers without error.

- [X] T010 [US2] Add stop logic to Makefile (docker-compose down)
- [X] T011 [US2] Document stop command in README.md

## Phase 5: User Story 3 (P3) - Quick Status Check

**Story Goal**: Operators can see service status quickly.
**Independent Test Criteria**: `make status` prints service state for each service.

- [X] T012 [US3] Implement status command in Makefile
- [X] T013 [US3] Document status command and sample output in README.md

## Phase 6: Polish & Cross-Cutting Concerns

**Goal**: Ensure docs and quickstart are aligned.
**Independent Test Criteria**: Quickstart includes start/stop/status steps.

- [X] T014 Update specs/001-one-command-start/quickstart.md with command examples
- [X] T015 Verify service status format aligns with specs/001-one-command-start/contracts/service-status.format.txt

## Dependencies

- US1 blocks US2 and US3.
- US2 and US3 can run in parallel after US1 completes.

## Parallel Execution Examples

- US2 and US3 tasks can run in parallel once compose services are defined.

## Implementation Strategy

- Start with docker-compose and Makefile scaffolding.
- Add backend/frontend services and health checks.
- Implement stop/status flows and documentation updates.
