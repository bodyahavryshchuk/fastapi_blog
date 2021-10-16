from pydantic import BaseSettings


class Settings(BaseSettings):
    db_url: str = ""

    class Config:
        env_prefix = ''
        env_file = '.env'
        env_file_encoding = 'utf-8'


settings = Settings()
