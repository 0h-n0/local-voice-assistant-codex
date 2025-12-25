# Research: Project Scaffold

**Date**: 2025-12-25
**Feature**: /home/relu/misc/local-voice-assistant-codex/specs/001-project-scaffold/spec.md

## Decisions

- Decision: Use Python 3.11 for the backend.
  Rationale: Stable runtime with broad FastAPI and uv support.
  Alternatives considered: Python 3.10, Python 3.12.

- Decision: Use Node.js 20 LTS for the frontend.
  Rationale: Current LTS compatible with Next.js and TypeScript tooling.
  Alternatives considered: Node.js 18 LTS.

- Decision: Use pytest for the backend health endpoint test.
  Rationale: Minimal critical-path coverage without extra tooling.
  Alternatives considered: unittest, no tests.

- Decision: Avoid database or external services in the scaffold.
  Rationale: Keeps the scaffold offline-first and minimal.
  Alternatives considered: SQLite, local cache.
