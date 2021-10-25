from pydantic import BaseSettings


class Settings(BaseSettings):
    SECRET_KEY: str = ""
    ACCESS_TOKEN_EXPIRE_HOURS: str = ""
    db_url: str = ""

    APPS_MODELS = [
        "user.models",
        "post.models",
        "aerich.models",
    ]

    class Config:
        env_prefix = ''
        env_file = '.env'
        env_file_encoding = 'utf-8'


settings = Settings()
