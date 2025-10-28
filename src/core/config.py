from pathlib import Path

from pydantic_settings import BaseSettings, SettingsConfigDict


class Config(BaseSettings):
    model_config = SettingsConfigDict(
        env_file=Path(__file__).parent.parent.parent / ".env",
        extra="ignore",
    )

    AWS_REGION: str
    AGENTS_MODEL_ID: str = "amazon.nova-lite-v1:0"


config = Config()  # type: ignore
