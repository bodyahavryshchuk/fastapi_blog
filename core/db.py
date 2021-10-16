import databases
from fastapi_users.db import SQLAlchemyUserDatabase
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import DeclarativeMeta, declarative_base

from core.settings import settings
from user.schemas import UserDB


engine = create_engine(
    settings.db_url, connect_args={"check_same_thread": False}
)
database = databases.Database(settings.db_url)
Base: DeclarativeMeta = declarative_base()


def get_user_db():
    from user.models import user
    yield SQLAlchemyUserDatabase(UserDB, database, user)
