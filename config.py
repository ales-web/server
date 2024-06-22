from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    db_username: str
    db_pass: str
    db_host: str
    db_port: str
    db_name: str
    s3_url: str
    s3_access_key: str
    s3_secret_access_key: str
    model_config = SettingsConfigDict(env_file=".env")


def get_settings():
    return Settings()


settings = Settings()
