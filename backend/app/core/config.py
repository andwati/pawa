from pydantic import BaseSettings

class Settings(BaseSettings):
    API_KEY: str
    GEMINI_API_URL: str
    ENVIRONMENT: str = "development"

    class Config:
        env_file = ".env"

settings = Settings()