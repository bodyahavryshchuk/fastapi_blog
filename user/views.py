from typing import List

from fastapi import APIRouter, Depends, HTTPException

from .models import User
from .permissions import is_superuser

from user import models, schemas, services

admin_router = APIRouter()


@admin_router.get('', response_model=List[schemas.UserPublic])
async def get_all_users(user: models.User = Depends(is_superuser)):
    return await User.all()


@admin_router.get('/{pk}', response_model=schemas.UserInDB)
async def get_single_user(pk: int, user: models.User = Depends(is_superuser)):
    user = await User.get(id=pk)
    if not user:
        return HTTPException(status_code=404)
    return user


@admin_router.post('', response_model=schemas.UserInDB)
async def create_user(schema: schemas.UserCreateInRegistration, user: models.User = Depends(is_superuser)):
    return await services.create_user(schema)


@admin_router.put('/{pk}', response_model=schemas.UserInDB)
async def update_user(pk: int, schema: schemas.UserUpdate, user: models.User = Depends(is_superuser)):
    return await services.update_user(schema, id=pk)


@admin_router.delete('/{pk}', status_code=204)
async def delete_user(pk: int, user: models.User = Depends(is_superuser)):
    return await services.delete_user(id=pk)
