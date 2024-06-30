from ninja import ModelSchema, Schema
from typing import Optional

from users.models import User


class UserRequestSchema(Schema):
    email: str
    password: str
    is_superuser: Optional[bool] = False


class UserResponseSchema(ModelSchema):
    class Meta:
        model = User
        fields = ["email"]
