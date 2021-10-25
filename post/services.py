from typing import TypeVar

from pydantic import BaseModel

from user.models import User
from .models import Category, Post

from .schemas import PostCreate, CategoryCreate, PostDetail

GetSchemaType = TypeVar("GetSchemaType", bound=BaseModel)


async def get_category_list():
    return await Category.all()


async def create_category(schema: CategoryCreate):
    return await Category.create(**schema.dict(exclude_unset=True))


async def get_post_list():
    return await PostDetail.from_queryset(Post.all())


async def get_post_detail(post_id):
    return await PostDetail.from_queryset_single(Post.get(id=post_id).prefetch_related('author'))


async def create_post(schema: PostCreate, user: User):
    return await Post.create(**schema.dict(exclude_unset=True), author=user)
