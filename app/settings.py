from pydantic import BaseSettings


class Settings(BaseSettings):
    MAX_RETRIES: int = 10


settings = Settings(_env_file='.env')  # type: ignore
