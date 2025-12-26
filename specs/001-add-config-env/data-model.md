# Data Model: Config Source Management

## Configuration Setting

- **key**: Canonical setting name (e.g., `OPENAI_API_KEY`, `MODEL_PATH`)
- **value**: Effective value as string (redacted if sensitive)
- **source**: One of `env`, `dotenv`, `config_file`, `default`
- **sensitive**: Boolean indicating whether the raw value must be redacted
- **description**: Optional human-readable description

## Effective Configuration

- **settings**: Collection of Configuration Setting entries
- **validated_at**: Timestamp of validation
- **version**: Schema version identifier for config summary output
