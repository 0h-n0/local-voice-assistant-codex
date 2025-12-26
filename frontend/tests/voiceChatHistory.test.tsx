import { act, render, screen, waitFor } from "@testing-library/react";
import userEvent from "@testing-library/user-event";
import { vi } from "vitest";

import { VoiceChatPage } from "../app/page";

vi.mock("../app/services/audioRecorder", () => ({
  AudioRecorder: class {
    start = vi.fn().mockResolvedValue(undefined);
    stop = vi.fn().mockResolvedValue(new Blob());
  },
}));

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

describe("conversation history", () => {
  it("renders multiple messages in order", async () => {
    const user = userEvent.setup();
    render(<VoiceChatPage />);

    await user.click(screen.getByRole("button", { name: "Start Recording" }));
    await user.click(screen.getByRole("button", { name: "Stop Recording" }));

    await act(async () => {
      onEvent?.({
        type: "transcript",
        payload: { text: "Hello", is_final: true },
      });
    });

    await user.click(screen.getByRole("button", { name: "Start Recording" }));
    await user.click(screen.getByRole("button", { name: "Stop Recording" }));

    await act(async () => {
      onEvent?.({
        type: "transcript",
        payload: { text: "Hi", is_final: true },
      });
    });

    await waitFor(() => {
      expect(screen.getAllByText("You").length).toBeGreaterThan(1);
    });
  });
});
