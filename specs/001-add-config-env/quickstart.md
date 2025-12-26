# Quickstart: Config Source Management

## Prerequisites

- Backend running locally
- Access to edit configuration sources

## Configure

1. Create a `.env` file at the repo root with a sample key:

   ```env
   OPENAI_API_KEY=example-key
   MODEL_PATH=/models/reazon
   AUDIO_DEVICE=default
   ```

2. Create a TOML config file at the repo root (default: `config.toml`):

   ```toml
   [llm]
   model="gpt-5-mini"

   [audio]
   device="default"
   ```

3. Set an environment variable override (takes precedence over .env and config file):

   ```sh
   export MODEL_PATH=/models/override
   ```

## Verify

1. Start the backend.
2. Call the config summary endpoint and confirm:
   - Values are resolved using env > .env > config file precedence.
   - Sensitive fields are redacted with `****`.

## Expected Results

- Configuration loads without errors.
- Validation errors include field names and reasons when invalid values are supplied.
