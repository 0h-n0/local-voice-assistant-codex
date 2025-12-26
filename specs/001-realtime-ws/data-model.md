# Data Model: Realtime Voice WebSocket

## StreamEvent

- **type**: status | transcript | response | audio
- **payload**: Event-specific data
- **timestamp**: Emission time

## StreamState

- **phase**: recording | transcribing | responding | idle
- **last_event_id**: Optional correlation identifier
