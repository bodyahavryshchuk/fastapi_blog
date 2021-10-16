from fastapi import APIRouter
from post import views


routes = APIRouter()

routes.include_router(views.router, prefix="/post")
