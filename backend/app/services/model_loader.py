from dataclasses import dataclass


@dataclass(frozen=True)
class SttModel:
    name: str


class ModelLoader:
    def load(self) -> SttModel:
        return SttModel(name="reazonspeech-nemo-v2")
