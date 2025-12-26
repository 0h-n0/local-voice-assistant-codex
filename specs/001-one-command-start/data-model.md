# Data Model: One-Command Service Startup

## Service

- **name**: Service identifier (e.g., backend, frontend)
- **command**: Start/stop command reference (compose service or make target)
- **ports**: Declared ports for reachability checks
- **required**: Boolean indicating whether service is required for a valid startup

## Service Status

- **name**: Service identifier
- **state**: running | stopped | failed
- **message**: Optional status detail (e.g., missing port, dependency failure)
