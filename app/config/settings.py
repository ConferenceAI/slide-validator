from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    app_name: str = "Slide Validator"
    admin_email: str = "admin@example.com"
    items_per_user: int = 50
    database_url: str = "sqlite:///./test.db"
    api_key: str = "your-api-key-here"

    model_config = SettingsConfigDict(env_file=".env")

settings = Settings()
