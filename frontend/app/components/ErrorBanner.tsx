type ErrorBannerProps = {
  message: string;
  onRetry?: () => void;
};

export const ErrorBanner = ({ message, onRetry }: ErrorBannerProps) => (
  <div
    style={{
      background: "#fee2e2",
      border: "1px solid #fecaca",
      padding: "0.75rem 1rem",
      borderRadius: "0.75rem",
      color: "#991b1b",
      display: "flex",
      justifyContent: "space-between",
      alignItems: "center",
      gap: "1rem",
    }}
  >
    <span>{message}</span>
    {onRetry ? (
      <button
        type="button"
        onClick={onRetry}
        style={{
          padding: "0.35rem 0.75rem",
          borderRadius: "999px",
          border: "1px solid #ef4444",
          color: "#ef4444",
          background: "transparent",
          cursor: "pointer",
          fontWeight: 600,
        }}
      >
        Retry
      </button>
    ) : null}
  </div>
);
