# Research: Voice Chat Web UI

## Decision 1: Recording interaction

**Decision**: Toggle start/stop recording.
**Rationale**: Matches common UI patterns and reduces accidental long recordings.
**Alternatives considered**: Hold-to-talk, auto-start.

## Decision 2: Audio playback control

**Decision**: Require explicit user action to play assistant audio.
**Rationale**: Aligns with privacy expectations and browser autoplay policies.
**Alternatives considered**: Auto-play, user setting toggle.

## Decision 3: Conversation scope

**Decision**: Single active conversation view.
**Rationale**: Keeps MVP focused and simplifies UI state.
**Alternatives considered**: Multiple conversations in sidebar.

## Decision 4: Recording display

**Decision**: Show recording indicator only, transcribe after stop.
**Rationale**: Keeps UI responsive and avoids partial states during capture.
**Alternatives considered**: Live waveform + transcript.

## Decision 5: History persistence

**Decision**: In-memory history cleared on reload.
**Rationale**: Minimizes data at rest and aligns with privacy goals.
**Alternatives considered**: Persist to local storage.

## Decision 6: Error presentation

**Decision**: Minimal banner + inline message.
**Rationale**: Keeps errors visible without blocking the flow.
**Alternatives considered**: Modal-only errors.
