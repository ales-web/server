from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    db_username: str
    db_pass: str
    db_host: str
    db_port: str
    db_name: str
    model_config = SettingsConfigDict(env_file=".env")


def get_settings():
    return Settings()


settings = Settings()
