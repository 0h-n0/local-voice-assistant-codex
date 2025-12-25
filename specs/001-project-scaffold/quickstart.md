# Quickstart: Project Scaffold

**Date**: 2025-12-25
**Feature**: /home/relu/misc/local-voice-assistant-codex/specs/001-project-scaffold/spec.md

## Prerequisites

- Python 3.11
- Node.js 20 LTS
- uv installed locally

## Backend (FastAPI)

1. Create and sync the environment:

   ```bash
   cd backend
   uv sync
   ```

2. Start the API:

   ```bash
   uv run uvicorn app.main:app --reload
   ```

3. Verify health endpoint:

   ```bash
   curl http://localhost:8000/health
   ```

## Frontend (Next.js)

1. Install dependencies:

   ```bash
   cd frontend
   npm install
   ```

2. Start the app:

   ```bash
   npm run dev
   ```

3. Open `http://localhost:3000` to see the status page.

## Quality Checks

- Backend lint:

  ```bash
  cd backend
  uv run ruff check .
  ```

- Backend tests:

  ```bash
  cd backend
  uv run pytest
  ```
