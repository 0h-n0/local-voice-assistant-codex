import { render, screen } from "@testing-library/react";
import userEvent from "@testing-library/user-event";
import { vi } from "vitest";

import { VoiceChatPage } from "../app/page";

vi.mock("../app/services/audioRecorder", () => ({
  AudioRecorder: class {
    start = vi.fn().mockResolvedValue(undefined);
    stop = vi.fn().mockResolvedValue(new Blob());
  },
}));

const callbacks: { onEvent?: (event: any) => void } = {};

vi.mock("../app/services/realtimeClient", () => ({
  RealtimeClient: class {
    connect = (cbs: any) => {
      callbacks.onEvent = cbs.onEvent;
    };
    sendAudio = vi.fn();
    sendEnd = vi.fn();
    disconnect = vi.fn();
  },
}));

describe("voice recording flow", () => {
  it("shows recording indicator when recording starts", async () => {
    const user = userEvent.setup();
    render(<VoiceChatPage />);

    await user.click(screen.getByRole("button", { name: "Start Recording" }));

    expect(screen.getByText("Recording...")).toBeInTheDocument();
  });
});
