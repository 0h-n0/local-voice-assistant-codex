import { render, screen, waitFor } from "@testing-library/react";
import userEvent from "@testing-library/user-event";
import { vi } from "vitest";

import { VoiceChatPage } from "../app/page";

vi.mock("../app/services/audioRecorder", () => ({
  AudioRecorder: class {
    start = vi.fn().mockResolvedValue(undefined);
    stop = vi.fn().mockResolvedValue(new Blob());
  },
}));

vi.mock("../app/services/chatApi", () => ({
  transcribeAudio: vi.fn().mockRejectedValue(new Error("fail")),
  requestAssistantReply: vi.fn(),
  synthesizeSpeech: vi.fn(),
}));

describe("error handling", () => {
  it("shows retry button when recording fails", async () => {
    const user = userEvent.setup();
    render(<VoiceChatPage />);

    await user.click(screen.getByRole("button", { name: "Start Recording" }));
    await user.click(screen.getByRole("button", { name: "Stop Recording" }));

    await waitFor(() => {
      expect(screen.getByRole("button", { name: "Retry" })).toBeInTheDocument();
    });
  });
});
