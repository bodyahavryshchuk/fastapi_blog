from typing import Optional

from fastapi import Form
from pydantic import BaseModel, EmailStr
from tortoise.contrib.pydantic import pydantic_model_creator
from .models import User


class UserBase(BaseModel):
    email: Optional[str] = None


class UserInDB(UserBase):
    id: int = None
    username: Optional[str] = None
    email: Optional[str] = None
    is_active: Optional[bool] = True
    is_superuser: Optional[bool] = False

    class Config:
        orm_mode = True


class UserCreate(UserInDB):
    username: str
    email: EmailStr
    password: str
    first_name: str
    avatar: str = None


class UserCreateInRegistration(BaseModel):
    username: str
    email: EmailStr
    password: str
    first_name: str
    avatar: str = None

    class Config:
        orm_mode = True


class UserUpdate(UserInDB):
    password: Optional[str] = Form(...)


class UserPublic(UserBase):
    id: int

    class Config:
        orm_mode = True


User_C_Pydantic = pydantic_model_creator(
    User, name='create_user', exclude_readonly=True, exclude=('is_active', 'is_staff', 'is_superuser'))
User_G_Pydantic = pydantic_model_creator(User, name='user')
