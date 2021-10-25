from fastapi import FastAPI
from core.db import database
from core.settings import settings
from routes import routes
from tortoise.contrib.fastapi import register_tortoise

app = FastAPI()


@app.on_event("startup")
async def startup():
    await database.connect()


@app.on_event("shutdown")
async def shutdown():
    await database.disconnect()


app.include_router(routes)


register_tortoise(
    app,
    db_url=settings.db_url,
    modules={"models": settings.APPS_MODELS},
    generate_schemas=True,
    add_exception_handlers=True,
)
