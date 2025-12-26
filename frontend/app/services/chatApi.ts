const API_BASE = process.env.NEXT_PUBLIC_API_BASE ?? "http://localhost:8000";

export const transcribeAudio = async (audio: Blob): Promise<string> => {
  const formData = new FormData();
  formData.append("file", audio, "recording.wav");
  formData.append("audio_format", "wav");

  const response = await fetch(`${API_BASE}/stt/file`, {
    method: "POST",
    body: formData,
  });
  if (!response.ok) {
    throw new Error("transcription_failed");
  }
  const payload = await response.json();
  return payload.text as string;
};

export const requestAssistantReply = async (prompt: string): Promise<string> => {
  const response = await fetch(`${API_BASE}/llm/complete`, {
    method: "POST",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify({ prompt }),
  });
  if (!response.ok) {
    throw new Error("llm_failed");
  }
  const payload = await response.json();
  return payload.text as string;
};

export const synthesizeSpeech = async (text: string): Promise<Blob> => {
  const response = await fetch(`${API_BASE}/tts/synthesize`, {
    method: "POST",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify({ text }),
  });
  if (!response.ok) {
    throw new Error("tts_failed");
  }
  const buffer = await response.arrayBuffer();
  return new Blob([buffer], { type: "audio/wav" });
};
