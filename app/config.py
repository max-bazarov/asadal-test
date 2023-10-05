from typing import Literal

from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    MODE: Literal["DEV", "PROD", "TEST"]
    LOG_LEVEL: Literal["INFO", "DEBUG"]

    REDIS_HOST: str
    REDIS_PORT: str

    model_config = SettingsConfigDict(env_file=".env", extra="allow")


settings = Settings()
