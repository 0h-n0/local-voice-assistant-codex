import { render, screen, waitFor } from "@testing-library/react";
import userEvent from "@testing-library/user-event";
import { vi } from "vitest";

import { VoiceChatPage } from "../app/page";

const playAudio = vi.fn();

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

vi.mock("../app/services/audioPlayer", () => ({
  playAudio: (...args: unknown[]) => playAudio(...args),
}));

describe("voice playback flow", () => {
  it("renders playback control and triggers play", async () => {
    const user = userEvent.setup();
    render(<VoiceChatPage />);

    await user.click(screen.getByRole("button", { name: "Start Recording" }));
    await user.click(screen.getByRole("button", { name: "Stop Recording" }));

    await waitFor(() => {
      expect(screen.getByText("Assistant")).toBeInTheDocument();
    });

    const playButton = screen.getByRole("button", { name: "Play audio" });
    await user.click(playButton);

    expect(playAudio).toHaveBeenCalled();
  });
});
