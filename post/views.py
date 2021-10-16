from typing import List

from fastapi import APIRouter, Depends, HTTPException

from user.auth import current_active_user, is_superuser
from user.models import User
from . import services
from .schemas import PostList, PostDetail, PostCreate, CategoryCreate, CategoryBase

router = APIRouter()


@router.get('/category', response_model=List[CategoryBase])
async def category_list():
    return await services.get_category_list()


@router.post('/category', status_code=201, response_model=CategoryBase)
async def post_create(item: CategoryCreate, user: User = Depends(is_superuser)):
    if not user:
        return HTTPException(status_code=403)
    return await services.create_category(item)


@router.get('/', response_model=List[PostList])
async def post_list():
    return await services.get_post_list()


@router.get('/{post_id}', response_model=PostDetail)
async def post_detail(post_id: int):
    post = await services.get_post_detail(post_id)
    if not post:
        raise HTTPException(status_code=404, detail='Post not found')
    return post


@router.post('/', status_code=201, response_model=PostDetail)
async def post_create(item: PostCreate, user: User = Depends(current_active_user)):
    return await services.create_post(item, user)

