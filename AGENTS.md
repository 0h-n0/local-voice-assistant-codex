# local-voice-assistant-codex Development Guidelines

Auto-generated from all feature plans. Last updated: 2025-12-26

## Active Technologies
- Python 3.11 (backend), Node.js 20 LTS (frontend), TypeScript 5.x + FastAPI, Pydantic, Uvicorn, uv, Ruff, reazon-research/reazonspeech-nemo-v2 (001-stt-api)
- N/A (no persistence required) (001-stt-api)
- Python 3.11 (backend), Node.js 20 LTS (frontend), TypeScript 5.x + FastAPI, Pydantic, Uvicorn, uv, Ruff, OpenAI API client (001-llm-service)
- N/A (no persistence) (001-llm-service)
- Python 3.11 (backend), Node.js 20 LTS (frontend), TypeScript 5.x + FastAPI, Pydantic, Uvicorn, uv, Ruff, Style-Bert-VITS2 (001-tts-api)
- N/A (no persistence) (001-tts-api)
- Python 3.11 + FastAPI, Pydantic v2, uv, Ruff (001-add-config-env)
- Local config file and environment variables (no database) (001-add-config-env)
- Python 3.11, Node.js 18+ + FastAPI, React/Next (TypeScript), uv, Ruff, docker-compose (001-one-command-start)
- Local filesystem and SQLite (existing components) (001-one-command-start)

- Python 3.11 (backend), Node.js 20 LTS (frontend), TypeScript 5.x + FastAPI, Pydantic, Uvicorn, uv, Ruff, Next.js, React (001-project-scaffold)

## Project Structure

```text
src/
tests/
```

## Commands

cd src [ONLY COMMANDS FOR ACTIVE TECHNOLOGIES][ONLY COMMANDS FOR ACTIVE TECHNOLOGIES] pytest [ONLY COMMANDS FOR ACTIVE TECHNOLOGIES][ONLY COMMANDS FOR ACTIVE TECHNOLOGIES] ruff check .

## Code Style

Python 3.11 (backend), Node.js 20 LTS (frontend), TypeScript 5.x: Follow standard conventions

## Recent Changes
- 001-one-command-start: Added Python 3.11, Node.js 18+ + FastAPI, React/Next (TypeScript), uv, Ruff, docker-compose
- 001-add-config-env: Added Python 3.11 + FastAPI, Pydantic v2, uv, Ruff
- 001-llm-service: Added Python 3.11 (backend), Node.js 20 LTS (frontend), TypeScript 5.x + FastAPI, Pydantic, Uvicorn, uv, Ruff, OpenAI API client


<!-- MANUAL ADDITIONS START -->
<!-- MANUAL ADDITIONS END -->
