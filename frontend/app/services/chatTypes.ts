export type Role = "user" | "assistant";

export type ChatMessage = {
  id: string;
  role: Role;
  content: string;
  audio?: Blob;
};

export type AudioClip = {
  id: string;
  kind: "input" | "output";
  blob: Blob;
};
