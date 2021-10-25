from fastapi import APIRouter

from auth.views import auth_router
from post.views import router
from user.views import admin_router


routes = APIRouter()

routes.include_router(router, prefix="/post")
routes.include_router(admin_router, prefix="/user", tags=['user'])
routes.include_router(auth_router, prefix="/auth", tags=['auth'])
