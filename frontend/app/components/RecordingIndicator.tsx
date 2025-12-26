type RecordingIndicatorProps = {
  active: boolean;
};

export const RecordingIndicator = ({ active }: RecordingIndicatorProps) => {
  if (!active) {
    return null;
  }
  return (
    <div
      style={{
        padding: "0.5rem 1rem",
        background: "#ffe4e6",
        borderRadius: "999px",
        color: "#9f1239",
        fontWeight: 600,
        display: "inline-flex",
        alignItems: "center",
        gap: "0.5rem",
      }}
    >
      <span
        style={{
          width: 10,
          height: 10,
          borderRadius: "50%",
          background: "#e11d48",
          display: "inline-block",
        }}
      />
      Recording...
    </div>
  );
};
