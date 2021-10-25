from tortoise import models, fields

from user.models import User


class Category(models.Model):
    name = fields.CharField(max_length=100)
    is_active = fields.BooleanField(default=True)
    posts: fields.ReverseRelation["Post"]

    class PydanticMeta:
        backward_relations = False


class Post(models.Model):
    category: fields.ForeignKeyRelation[Category] = fields.ForeignKeyField(
        "models.Category", on_delete=fields.CASCADE, related_name="posts"
    )
    author: fields.ForeignKeyRelation[User] = fields.ForeignKeyField(
        "models.User", on_delete=fields.CASCADE, related_name="posts"
    )
    title = fields.CharField(max_length=100)
    text = fields.TextField()
    created_dt = fields.DatetimeField(auto_now_add=True)

    class PydanticMeta:
        backward_relations = False
