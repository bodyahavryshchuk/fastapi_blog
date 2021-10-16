from datetime import datetime
from typing import Optional

from pydantic import BaseModel

from user.schemas import UserInPost


class CategoryBase(BaseModel):
    id: Optional[int]
    name: str


class CategoryCreate(CategoryBase):
    is_active: bool

    class Config:
        orm_mode = True


class PostBase(BaseModel):
    id: Optional[int]
    category: Optional[int]
    title: str
    text: str


class PostList(PostBase):
    created_dt: Optional[datetime]
    # user: UserInPost


class PostDetail(PostList):
   author: UserInPost


class PostCreate(PostBase):
    category: int

    class Config:
        orm_mode = True
