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

vi.mock("../app/services/chatApi", () => ({
  transcribeAudio: vi.fn().mockResolvedValue("Hello"),
  requestAssistantReply: vi.fn().mockResolvedValue("Hi there"),
  synthesizeSpeech: vi.fn().mockResolvedValue(new Blob()),
}));

describe("voice recording flow", () => {
  it("shows recording indicator when recording starts", async () => {
    const user = userEvent.setup();
    render(<VoiceChatPage />);

    await user.click(screen.getByRole("button", { name: "Start Recording" }));

    expect(screen.getByText("Recording...")).toBeInTheDocument();
  });
});
