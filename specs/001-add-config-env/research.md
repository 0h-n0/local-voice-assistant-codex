# Research: Config Source Management

## Decision 1: Configuration loading approach

**Decision**: Use Pydantic v2 settings via `pydantic-settings` for structured loading
from environment variables and .env, and merge with a config file loader.

**Rationale**: Pydantic settings provide validation, env parsing, and typed defaults
aligned with existing schema usage. It keeps validation consistent with current
Pydantic models and avoids ad-hoc parsing.

**Alternatives considered**:
- Manual `os.environ` parsing (lower dependencies but more error-prone)
- `python-dotenv` only (does not cover typed validation)

## Decision 2: Config file format

**Decision**: Use a single TOML config file parsed with Python 3.11 `tomllib`.

**Rationale**: TOML is human-readable, deterministic, and supported by the standard
library in Python 3.11 without introducing a new dependency.

**Alternatives considered**:
- YAML (requires PyYAML dependency)
- JSON (less ergonomic for configuration comments)

## Decision 3: Redaction strategy

**Decision**: Redact sensitive values in summaries using a fixed mask (`****`).

**Rationale**: Simple, predictable, and avoids accidental leakage of secrets.

**Alternatives considered**:
- Partial reveal (risk of leakage and inconsistent behavior)
- Omit fields entirely (reduces visibility for operators)
