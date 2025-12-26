import { act, render, screen } from "@testing-library/react";
import userEvent from "@testing-library/user-event";
import { vi } from "vitest";

import { VoiceChatPage } from "../app/page";

const playAudio = vi.fn();
let onEvent: ((event: any) => void) | undefined;
let onAudio: ((audio: Blob) => void) | undefined;

vi.mock("../app/services/realtimeClient", () => ({
  RealtimeClient: class {
    connect = (cbs: any) => {
      onEvent = cbs.onEvent;
      onAudio = cbs.onAudio;
    };
    sendAudio = vi.fn();
    sendEnd = vi.fn();
    disconnect = vi.fn();
  },
}));

vi.mock("../app/services/audioPlayer", () => ({
  playAudio: (...args: unknown[]) => playAudio(...args),
}));

vi.mock("../app/services/audioRecorder", () => ({
  AudioRecorder: class {
    start = vi.fn().mockResolvedValue(undefined);
    stop = vi.fn().mockResolvedValue(new Blob());
  },
}));

describe("realtime playback", () => {
  it("shows play button for audio events", async () => {
    const user = userEvent.setup();
    render(<VoiceChatPage />);

    await user.click(screen.getByRole("button", { name: "Start Recording" }));

    await act(async () => {
      onEvent?.({ type: "response", payload: { text: "hello" } });
    });
    await act(async () => {
      onAudio?.(new Blob([new Uint8Array([1])], { type: "audio/wav" }));
    });

    const playButton = await screen.findByRole("button", {
      name: "Play audio",
    });
    await user.click(playButton);

    expect(playAudio).toHaveBeenCalled();
  });
});
