import os
from dotenv import load_dotenv

load_dotenv()


class Settings:

    OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")

    MODEL_NAME = os.getenv("MODEL_NAME", "gpt-5.5")

    DATABASE_URL = os.getenv(
        "DATABASE_URL",
        "postgresql+asyncpg://postgres:postgres@localhost:5432/crawler_db"
    )


settings = Settings()