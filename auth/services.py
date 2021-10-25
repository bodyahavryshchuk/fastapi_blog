import jwt
from jwt.exceptions import InvalidTokenError
from datetime import datetime, timedelta
from typing import Optional

from passlib.context import CryptContext
from tortoise.query_utils import Q

from core.settings import settings

from user import schemas, services
from user.models import User

password_reset_jwt_subject = "preset"


async def registration_user(new_user: schemas.UserCreateInRegistration):
    if await User.filter(Q(username=new_user.username) | Q(email=new_user.email)).exists():
        return True
    else:
        user = await services.create_user(new_user)
        return False


def generate_password_reset_token(email: str):
    delta = timedelta(hours=settings.EMAIL_RESET_TOKEN_EXPIRE_HOURS)
    now = datetime.utcnow()
    expires = now + delta
    exp = expires.timestamp()
    encoded_jwt = jwt.encode(
        {"exp": exp, "nbf": now, "sub": password_reset_jwt_subject, "email": email},
        settings.SECRET_KEY,
        algorithm="HS256",
    )
    return encoded_jwt


def verify_password_reset_token(token: str) -> Optional[str]:
    try:
        decoded_token = jwt.decode(token, settings.SECRET_KEY, algorithms=["HS256"])
        assert decoded_token["sub"] == password_reset_jwt_subject
        return decoded_token["email"]
    except InvalidTokenError:
        return None


async def authenticate(username: str, password: str):
    user = await User.get(username=username)
    if not user:
        return None

    pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")
    if not pwd_context.verify(password, user.password):
        return None
    return user
