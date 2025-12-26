export type StreamStatus = "recording" | "transcribing" | "responding" | "idle" | "error";

export type StatusPayload = {
  state: StreamStatus;
  code?: string;
  message?: string;
};

export type TranscriptPayload = {
  text: string;
  is_final: boolean;
};

export type ResponsePayload = {
  text: string;
};

export type AudioPayload = {
  format: string;
  size: number;
};

export type StreamEvent =
  | { type: "status"; payload: StatusPayload }
  | { type: "transcript"; payload: TranscriptPayload }
  | { type: "response"; payload: ResponsePayload }
  | { type: "audio"; payload: AudioPayload };
