from pydantic import BaseModel


class ConfigSetting(BaseModel):
    key: str
    value: str
    source: str
    sensitive: bool
    description: str | None = None


class ConfigSummary(BaseModel):
    settings: list[ConfigSetting]
    validated_at: str
    version: str
