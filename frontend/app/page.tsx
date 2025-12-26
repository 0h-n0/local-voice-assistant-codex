"use client";

import { useRef, useState } from "react";

import { ChatMessage } from "./components/ChatMessage";
import { ErrorBanner } from "./components/ErrorBanner";
import { PlaybackControls } from "./components/PlaybackControls";
import { RecordingIndicator } from "./components/RecordingIndicator";
import { playAudio } from "./services/audioPlayer";
import { AudioRecorder } from "./services/audioRecorder";
import { requestAssistantReply, synthesizeSpeech, transcribeAudio } from "./services/chatApi";
import type { ChatMessage as ChatMessageType } from "./services/chatTypes";

export function VoiceChatPage() {
  const recorderRef = useRef(new AudioRecorder());
  const [messages, setMessages] = useState<ChatMessageType[]>([]);
  const [isRecording, setIsRecording] = useState(false);
  const [isProcessing, setIsProcessing] = useState(false);
  const [error, setError] = useState<string | null>(null);

  const handleStart = async () => {
    setError(null);
    try {
      await recorderRef.current.start();
      setIsRecording(true);
    } catch (err) {
      setError("Failed to start recording.");
    }
  };

  const handleStop = async () => {
    setIsRecording(false);
    setIsProcessing(true);
    try {
      const audio = await recorderRef.current.stop();
      const transcript = await transcribeAudio(audio);
      const userMessage: ChatMessageType = {
        id: `user-${Date.now()}`,
        role: "user",
        content: transcript,
      };
      setMessages((prev) => [...prev, userMessage]);

      const assistantText = await requestAssistantReply(transcript);
      const assistantAudio = await synthesizeSpeech(assistantText);
      const assistantMessage: ChatMessageType = {
        id: `assistant-${Date.now()}`,
        role: "assistant",
        content: assistantText,
        audio: assistantAudio,
      };
      setMessages((prev) => [...prev, assistantMessage]);
    } catch (err) {
      setError("Recording or playback failed. Please retry.");
    } finally {
      setIsProcessing(false);
    }
  };

  const handleRetry = () => {
    setError(null);
  };

  return (
    <main
      style={{
        padding: "2rem",
        fontFamily: "Arial, sans-serif",
        background: "#f8fafc",
        minHeight: "100vh",
      }}
    >
      <h1 style={{ marginBottom: "0.5rem" }}>Local Voice Assistant</h1>
      <p style={{ marginTop: 0, color: "#475569" }}>
        Speak to the assistant and review the conversation history.
      </p>

      {error ? <ErrorBanner message={error} onRetry={handleRetry} /> : null}

      <section style={{ marginTop: "1.5rem" }}>
        <RecordingIndicator active={isRecording} />
        <div style={{ marginTop: "1rem", display: "flex", gap: "1rem" }}>
          <button
            type="button"
            onClick={isRecording ? handleStop : handleStart}
            disabled={isProcessing}
            style={{
              padding: "0.75rem 1.5rem",
              borderRadius: "999px",
              border: "none",
              background: isRecording ? "#ef4444" : "#2563eb",
              color: "white",
              fontWeight: 600,
              cursor: "pointer",
            }}
          >
            {isRecording ? "Stop Recording" : "Start Recording"}
          </button>
          {isProcessing ? (
            <span style={{ color: "#0f172a" }}>Processing...</span>
          ) : null}
        </div>
        {error ? (
          <div style={{ marginTop: "0.5rem", color: "#b91c1c" }}>{error}</div>
        ) : null}
      </section>

      <section
        style={{
          marginTop: "2rem",
          display: "flex",
          flexDirection: "column",
          gap: "1rem",
          maxHeight: "60vh",
          overflowY: "auto",
          paddingRight: "0.5rem",
        }}
      >
        {messages.map((message) => (
          <div key={message.id}>
            <ChatMessage message={message} />
            {message.role === "assistant" && message.audio ? (
              <PlaybackControls onPlay={() => playAudio(message.audio!)} />
            ) : null}
          </div>
        ))}
        {messages.length === 0 ? (
          <div style={{ color: "#94a3b8" }}>No messages yet.</div>
        ) : null}
      </section>
    </main>
  );
}

export default VoiceChatPage;
