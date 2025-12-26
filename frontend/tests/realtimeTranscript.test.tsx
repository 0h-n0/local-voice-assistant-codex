import { act, render, screen } from "@testing-library/react";
import userEvent from "@testing-library/user-event";
import { vi } from "vitest";

import { VoiceChatPage } from "../app/page";

let onEvent: ((event: any) => void) | undefined;

vi.mock("../app/services/realtimeClient", () => ({
  RealtimeClient: class {
    connect = (cbs: any) => {
      onEvent = cbs.onEvent;
    };
    sendAudio = vi.fn();
    sendEnd = vi.fn();
    disconnect = vi.fn();
  },
}));

vi.mock("../app/services/audioRecorder", () => ({
  AudioRecorder: class {
    start = vi.fn().mockResolvedValue(undefined);
    stop = vi.fn().mockResolvedValue(new Blob());
  },
}));

describe("realtime transcript", () => {
  it("renders live transcript updates", async () => {
    const user = userEvent.setup();
    render(<VoiceChatPage />);

    await user.click(screen.getByRole("button", { name: "Start Recording" }));

    await act(async () => {
      onEvent?.({
        type: "transcript",
        payload: { text: "partial text", is_final: false },
      });
    });

    expect(
      await screen.findByText(/Live transcript: partial text/)
    ).toBeInTheDocument();
  });
});
