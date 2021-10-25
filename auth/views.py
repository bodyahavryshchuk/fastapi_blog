from fastapi import APIRouter, Depends, HTTPException
from fastapi.security import OAuth2PasswordRequestForm

from user import schemas

from .schemas import Token
from .jwt import create_token
from .services import registration_user, authenticate

auth_router = APIRouter()


@auth_router.post("/login/access-token", response_model=Token)
async def login_access_token(form_data: OAuth2PasswordRequestForm = Depends()):
    user = await authenticate(username=form_data.username, password=form_data.password)
    if not user:
        raise HTTPException(status_code=400, detail="Incorrect username or password")
    elif not user.is_active:
        raise HTTPException(status_code=400, detail="Inactive user")
    return create_token(user.id)


@auth_router.post("/registration", response_model=schemas.UserInDB)
async def user_registration(new_user: schemas.UserCreateInRegistration):
    user = await registration_user(new_user)
    if user:
        raise HTTPException(status_code=400, detail="User already exists")
    else:
        return user
