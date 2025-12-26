type PlaybackControlsProps = {
  onPlay: () => void;
};

export const PlaybackControls = ({ onPlay }: PlaybackControlsProps) => (
  <button
    type="button"
    onClick={onPlay}
    style={{
      marginTop: "0.5rem",
      padding: "0.4rem 0.75rem",
      borderRadius: "999px",
      border: "1px solid #0ea5e9",
      color: "#0ea5e9",
      background: "transparent",
      cursor: "pointer",
      fontWeight: 600,
    }}
  >
    Play audio
  </button>
);
