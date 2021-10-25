from fastapi_users.password import get_password_hash

from user import schemas
from user.models import User


async def create_user(schema: schemas.UserCreateInRegistration):
    hash_password = get_password_hash(schema.dict().pop("password"))
    return await User.create(
            **schema.dict(exclude={"password"}, exclude_unset=True),
            password=hash_password
        )


async def update_user(schema: schemas.UserUpdate, id: int):
    return await User.filter(id=id).update(**schema.dict(exclude_unset=True))


async def delete_user(id: int):
    return await User.filter(id=id).delete()
