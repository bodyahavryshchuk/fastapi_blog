from datetime import datetime
from typing import Optional

from pydantic import BaseModel
from tortoise.contrib.pydantic import pydantic_model_creator, PydanticModel

from user.schemas import UserPublic


class CategoryBase(BaseModel):
    id: Optional[int]
    name: str

    class Config:
        orm_mode = True


class CategoryCreate(CategoryBase):
    is_active: bool

    class Config:
        orm_mode = True


class PostBase(PydanticModel):
    id: Optional[int]
    category: Optional[int]
    title: str
    text: str


class PostList(PostBase):
    created_dt: Optional[datetime]
    # user: UserInPost


class PostDetail(PydanticModel):
    id: int
    category: CategoryBase
    author: UserPublic
    title: str
    text: str
    created_dt: datetime


class PostCreate(PostBase):

    class Config:
        orm_mode = True

# PostCreate = pydantic_model_creator(
#     Post,
#     exclude_readonly=True,
# )


# PostD = pydantic_model_creator(Post, name="get_post")