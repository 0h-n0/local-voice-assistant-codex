export const playAudio = (audio: Blob): HTMLAudioElement => {
  const url = URL.createObjectURL(audio);
  const element = new Audio(url);
  element.onended = () => URL.revokeObjectURL(url);
  element.onerror = () => URL.revokeObjectURL(url);
  void element.play();
  return element;
};
