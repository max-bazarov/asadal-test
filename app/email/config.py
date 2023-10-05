from pydantic_settings import BaseSettings, SettingsConfigDict


class EmailConfig(BaseSettings):
    MAIL_USERNAME: str
    MAIL_PASSWORD: str
    MAIL_FROM: str
    MAIL_PORT: str
    MAIL_SERVER: str
    MAIL_FROM_NAME: str

    model_config = SettingsConfigDict(env_file=".env", extra="allow")


email_config = EmailConfig()
