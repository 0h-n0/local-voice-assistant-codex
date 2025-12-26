# Research: Realtime Voice WebSocket

## Decision 1: WebSocket payloads

**Decision**: Text events + audio frames over WebSocket.
**Rationale**: Supports real-time UI updates without extra HTTP calls.
**Alternatives considered**: Text-only WebSocket with HTTP audio.

## Decision 2: Authentication

**Decision**: Token via Sec-WebSocket-Protocol.
**Rationale**: Compatible with browser WebSocket APIs and avoids query tokens.
**Alternatives considered**: Query string token, no auth.

## Decision 3: Transcript updates

**Decision**: Partial updates + final transcript.
**Rationale**: Provides immediate feedback with a final definitive transcript.
**Alternatives considered**: Final only.

## Decision 4: Reconnect behavior

**Decision**: Auto-reconnect without resume (restart stream).
**Rationale**: Simpler client state handling with predictable recovery.
**Alternatives considered**: Resume from last timestamp, manual retry.

## Decision 5: Audio framing

**Decision**: WAV chunks, 100–200ms.
**Rationale**: Balances latency and overhead; fits local processing.
**Alternatives considered**: Larger chunks.

## Decision 6: Event types

**Decision**: status, transcript, response, audio.
**Rationale**: Minimal set for UI updates and playback.
**Alternatives considered**: Expanded status taxonomy.
