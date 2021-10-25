import databases
from fastapi_users.db import SQLAlchemyUserDatabase
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import DeclarativeMeta, declarative_base

from core.settings import settings

#
# engine = create_engine(
#     settings.db_url, connect_args={"check_same_thread": False}
# )
database = databases.Database(settings.db_url)
Base: DeclarativeMeta = declarative_base()


TORTOISE_ORM = {
    "connections": {"default": settings.db_url},
    "apps": {
        "models": {
            "models": settings.APPS_MODELS,
            "default_connection": "default",
        }
    },
}