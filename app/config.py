from pydantic.v1 import BaseSettings


class Settings(BaseSettings):
    api_key: str
    external_api_url: str

    class Config:
        env_file = ".env"


settings = Settings()
