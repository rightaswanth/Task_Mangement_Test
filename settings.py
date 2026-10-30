from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    app_name: str = "Task Manger"
    database_url: str
    debug: bool

    class Config:
        env_file=".env"


settings = Settings()