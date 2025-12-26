import type { StreamEvent } from "./realtimeTypes";

type RealtimeCallbacks = {
  onEvent: (event: StreamEvent) => void;
  onAudio: (audio: Blob) => void;
  onClose?: () => void;
};

export class RealtimeClient {
  private url: string;
  private token?: string;
  private ws: WebSocket | null = null;
  private callbacks: RealtimeCallbacks | null = null;
  private shouldReconnect = true;

  constructor(url: string, token?: string) {
    this.url = url;
    this.token = token;
  }

  connect(callbacks: RealtimeCallbacks) {
    this.callbacks = callbacks;
    const ws = new WebSocket(this.url, this.token ? [this.token] : undefined);
    ws.binaryType = "arraybuffer";
    ws.onmessage = (message) => {
      if (typeof message.data === "string") {
        const event = JSON.parse(message.data) as StreamEvent;
        this.callbacks?.onEvent(event);
      } else {
        const blob =
          message.data instanceof Blob
            ? message.data
            : new Blob([message.data], { type: "audio/wav" });
        this.callbacks?.onAudio(blob);
      }
    };
    ws.onclose = () => {
      this.ws = null;
      this.callbacks?.onClose?.();
      if (this.shouldReconnect) {
        setTimeout(() => this.connect(callbacks), 1000);
      }
    };
    this.ws = ws;
  }

  sendAudio(chunk: Blob) {
    if (this.ws?.readyState === WebSocket.OPEN) {
      this.ws.send(chunk);
    }
  }

  sendEnd() {
    if (this.ws?.readyState === WebSocket.OPEN) {
      this.ws.send(JSON.stringify({ event: "end" }));
    }
  }

  disconnect() {
    this.shouldReconnect = false;
    this.ws?.close();
  }
}
