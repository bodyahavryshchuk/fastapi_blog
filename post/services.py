from sqlalchemy import select

from core.db import database
from .models import post, category
from user.models import User, user

from .schemas import PostCreate, CategoryCreate


async def get_category_list():
    category_list = await database.fetch_all(query=category.select())
    return [dict(result) for result in category_list]


async def create_category(item: CategoryCreate):
    new_category = category.insert().values(**item.dict())
    pk = await database.execute(new_category)
    return {**item.dict()}


async def get_post_list():
    post_list = await database.fetch_all(query=post.select())
    return [dict(result) for result in post_list]


async def get_post_detail(post_id):
    u = user.alias('user')
    p = post.alias('post')
    q = select([u.c.id.label('userId'), u.c.email.label('userEmail'), p]) \
        .select_from(p.join(u))\
        .where((p.c.id == post_id) & (u.c.id == p.c.user))
    post_detail = await database.fetch_one(q)
    if post_detail is not None:
        post_detail = dict(post_detail)
        return {**post_detail, 'author': {'id': str(post_detail.pop('userId')), 'email': post_detail.pop('userEmail')}}
    return None


async def create_post(item: PostCreate, user: User):
    new_post = post.insert().values(**item.dict(), user=user.id)
    pk = await database.execute(new_post)
    return {**item.dict(), 'user': {'id': user.id}}
