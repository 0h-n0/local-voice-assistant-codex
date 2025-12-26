type RecorderState = {
  stream: MediaStream;
  context: AudioContext;
  processor: ScriptProcessorNode;
  chunks: Float32Array[];
  onChunk?: (chunk: Blob) => void;
};

export class AudioRecorder {
  private state: RecorderState | null = null;

  async start(onChunk?: (chunk: Blob) => void): Promise<void> {
    if (this.state) {
      return;
    }
    const stream = await navigator.mediaDevices.getUserMedia({ audio: true });
    const context = new AudioContext();
    const source = context.createMediaStreamSource(stream);
    const processor = context.createScriptProcessor(4096, 1, 1);
    const chunks: Float32Array[] = [];

    processor.onaudioprocess = (event) => {
      const input = event.inputBuffer.getChannelData(0);
      chunks.push(new Float32Array(input));
      if (onChunk) {
        const wavBuffer = encodeWav(new Float32Array(input), context.sampleRate);
        onChunk(new Blob([wavBuffer], { type: "audio/wav" }));
      }
    };

    source.connect(processor);
    processor.connect(context.destination);

    this.state = { stream, context, processor, chunks, onChunk };
  }

  async stop(): Promise<Blob> {
    if (!this.state) {
      throw new Error("not_recording");
    }
    const { stream, context, processor, chunks } = this.state;
    processor.disconnect();
    await context.close();
    stream.getTracks().forEach((track) => track.stop());
    this.state = null;

    const merged = mergeChunks(chunks);
    const wavBuffer = encodeWav(merged, context.sampleRate);
    return new Blob([wavBuffer], { type: "audio/wav" });
  }
}

const mergeChunks = (chunks: Float32Array[]): Float32Array => {
  const totalLength = chunks.reduce((sum, chunk) => sum + chunk.length, 0);
  const result = new Float32Array(totalLength);
  let offset = 0;
  for (const chunk of chunks) {
    result.set(chunk, offset);
    offset += chunk.length;
  }
  return result;
};

const encodeWav = (samples: Float32Array, sampleRate: number): ArrayBuffer => {
  const buffer = new ArrayBuffer(44 + samples.length * 2);
  const view = new DataView(buffer);

  writeString(view, 0, "RIFF");
  view.setUint32(4, 36 + samples.length * 2, true);
  writeString(view, 8, "WAVE");
  writeString(view, 12, "fmt ");
  view.setUint32(16, 16, true);
  view.setUint16(20, 1, true);
  view.setUint16(22, 1, true);
  view.setUint32(24, sampleRate, true);
  view.setUint32(28, sampleRate * 2, true);
  view.setUint16(32, 2, true);
  view.setUint16(34, 16, true);
  writeString(view, 36, "data");
  view.setUint32(40, samples.length * 2, true);

  let offset = 44;
  for (let i = 0; i < samples.length; i += 1) {
    const s = Math.max(-1, Math.min(1, samples[i]));
    view.setInt16(offset, s < 0 ? s * 0x8000 : s * 0x7fff, true);
    offset += 2;
  }

  return buffer;
};

const writeString = (view: DataView, offset: number, value: string): void => {
  for (let i = 0; i < value.length; i += 1) {
    view.setUint8(offset + i, value.charCodeAt(i));
  }
};
