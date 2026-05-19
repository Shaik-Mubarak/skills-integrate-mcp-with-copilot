from typing import List

from pydantic import BaseSettings, Field


class Settings(BaseSettings):
    app_name: str = Field("Mergington High School API", env="APP_NAME")
    environment: str = Field("development", env="APP_ENV")
    debug: bool = Field(True, env="DEBUG")
    secret_key: str = Field("dev-secret-key", env="SECRET_KEY")
    database_url: str = Field("sqlite:///./data/app.db", env="DATABASE_URL")
    static_dir: str = Field("static", env="STATIC_DIR")
    allowed_hosts: List[str] = Field(["*"], env="ALLOWED_HOSTS")

    class Config:
        env_file = ".env"
        env_file_encoding = "utf-8"


settings = Settings()
