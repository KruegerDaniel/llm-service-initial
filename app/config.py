from pydantic.v1 import BaseSettings


class Settings(BaseSettings):
    api_key: str
    ollama_host: str

    class Config:
        env_file = ".env"


settings = Settings()
