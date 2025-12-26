"use client";

import { useMemo, useRef, useState } from "react";

import { ChatMessage } from "./components/ChatMessage";
import { ErrorBanner } from "./components/ErrorBanner";
import { PlaybackControls } from "./components/PlaybackControls";
import { RecordingIndicator } from "./components/RecordingIndicator";
import { playAudio } from "./services/audioPlayer";
import { AudioRecorder } from "./services/audioRecorder";
import { RealtimeClient } from "./services/realtimeClient";
import type { ChatMessage as ChatMessageType } from "./services/chatTypes";
import type { StreamEvent, StreamStatus } from "./services/realtimeTypes";

export function VoiceChatPage() {
  const recorderRef = useRef(new AudioRecorder());
  const audioChunksRef = useRef<Blob[]>([]);
  const lastAssistantIdRef = useRef<string | null>(null);
  const clientRef = useRef<RealtimeClient | null>(null);
  const [messages, setMessages] = useState<ChatMessageType[]>([]);
  const [isRecording, setIsRecording] = useState(false);
  const [status, setStatus] = useState<StreamStatus>("idle");
  const [partialTranscript, setPartialTranscript] = useState("");
  const [error, setError] = useState<string | null>(null);
  const isBusy = status !== "idle" && !isRecording;

  const wsUrl = useMemo(
    () => process.env.NEXT_PUBLIC_WS_URL ?? "ws://localhost:8000/ws/voice",
    []
  );
  const wsToken = useMemo(() => process.env.NEXT_PUBLIC_WS_TOKEN, []);

  const attachAudioToLastAssistant = (audio: Blob) => {
    const targetId = lastAssistantIdRef.current;
    if (!targetId) {
      audioChunksRef.current.push(audio);
      return;
    }
    setMessages((prev) =>
      prev.map((message) =>
        message.id === targetId ? { ...message, audio } : message
      )
    );
    lastAssistantIdRef.current = null;
  };

  const handleEvent = (event: StreamEvent) => {
    if (event.type === "status") {
      setStatus(event.payload.state);
      if (event.payload.state === "error") {
        setError(event.payload.message ?? "Streaming error.");
      }
      return;
    }

    if (event.type === "transcript") {
      if (event.payload.is_final) {
        const finalMessage: ChatMessageType = {
          id: `user-${Date.now()}`,
          role: "user",
          content: event.payload.text,
        };
        setMessages((prev) => [...prev, finalMessage]);
        setPartialTranscript("");
      } else {
        setPartialTranscript(event.payload.text);
      }
      return;
    }

    if (event.type === "response") {
      const assistantMessage: ChatMessageType = {
        id: `assistant-${Date.now()}`,
        role: "assistant",
        content: event.payload.text,
      };
      setMessages((prev) => [...prev, assistantMessage]);
      lastAssistantIdRef.current = assistantMessage.id;
      if (audioChunksRef.current.length) {
        const audio = new Blob(audioChunksRef.current, { type: "audio/wav" });
        audioChunksRef.current = [];
        attachAudioToLastAssistant(audio);
      }
      return;
    }
  };

  const handleAudio = (audio: Blob) => {
    attachAudioToLastAssistant(audio);
  };

  const connectClient = () => {
    if (clientRef.current) {
      return;
    }
    const client = new RealtimeClient(wsUrl, wsToken);
    client.connect({
      onEvent: handleEvent,
      onAudio: handleAudio,
      onClose: () => setStatus("idle"),
    });
    clientRef.current = client;
  };

  const handleStart = async () => {
    setError(null);
    try {
      connectClient();
      await recorderRef.current.start((chunk) => clientRef.current?.sendAudio(chunk));
      setIsRecording(true);
    } catch (err) {
      setError("Failed to start recording.");
    }
  };

  const handleStop = async () => {
    setIsRecording(false);
    try {
      await recorderRef.current.stop();
      clientRef.current?.sendEnd();
    } catch (err) {
      setError("Recording or playback failed. Please retry.");
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
        {status !== "idle" ? (
          <div style={{ marginTop: "0.5rem", color: "#475569" }}>
            Status: {status}
          </div>
        ) : null}
        <div style={{ marginTop: "1rem", display: "flex", gap: "1rem" }}>
          <button
            type="button"
            onClick={isRecording ? handleStop : handleStart}
            disabled={isBusy}
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
        </div>
        {error ? (
          <div style={{ marginTop: "0.5rem", color: "#b91c1c" }}>{error}</div>
        ) : null}
        {partialTranscript ? (
          <div style={{ marginTop: "0.5rem", color: "#0f172a" }}>
            Live transcript: {partialTranscript}
          </div>
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
