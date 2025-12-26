import type { ChatMessage } from "../services/chatTypes";

type ChatMessageProps = {
  message: ChatMessage;
};

export const ChatMessage = ({ message }: ChatMessageProps) => {
  const isUser = message.role === "user";
  return (
    <div
      style={{
        alignSelf: isUser ? "flex-end" : "flex-start",
        background: isUser ? "#e0f2fe" : "#f1f5f9",
        color: "#0f172a",
        padding: "0.75rem 1rem",
        borderRadius: "1rem",
        maxWidth: "70%",
        whiteSpace: "pre-wrap",
      }}
    >
      <div style={{ fontSize: "0.75rem", opacity: 0.6, marginBottom: "0.25rem" }}>
        {isUser ? "You" : "Assistant"}
      </div>
      <div>{message.content}</div>
    </div>
  );
};
