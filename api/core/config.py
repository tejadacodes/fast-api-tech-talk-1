from pydantic import BaseSettings


class Settings(BaseSettings):
    app_db_url: str = "postgresql://user:password@server:port/db"



settings = Settings()