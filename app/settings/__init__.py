from dotenv import load_dotenv
from pydantic import BaseSettings

load_dotenv()


class Settings(BaseSettings):
    MAX_RETRIES: int = 10


settings = Settings()  # type: ignore
