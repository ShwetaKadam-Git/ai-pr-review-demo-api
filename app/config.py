import os


class Settings:
    database_url: str = os.environ.get("DATABASE_URL", "sqlite:///./reviews.db")
    api_key: str = os.environ.get("API_KEY", "")
    ai_mode: str = os.environ.get("AI_MODE", "mock")


settings = Settings()