from pydantic import field_validator
from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    """Application configuration settings loaded from environment variables."""

    PROJECT_NAME: str = "LoanGuard API"
    API_V1_STR: str = "/api/v1"
    ENVIRONMENT: str = "development"
    DEBUG: bool = True

    # Database connection placeholder
    DATABASE_URL: str = "sqlite:///./loanguard.db"

    @field_validator("DEBUG", mode="before")
    @classmethod
    def parse_debug(cls, v: object) -> bool:
        if isinstance(v, str):
            return v.lower() in ("true", "1", "t", "yes", "debug", "dev", "development")
        return bool(v)

    model_config = SettingsConfigDict(
        env_file=".env",
        env_file_encoding="utf-8",
        extra="ignore",
    )


settings = Settings()
