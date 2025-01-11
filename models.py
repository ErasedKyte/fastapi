from tortoise import Model, fields
from datetime import datetime
from pydantic import BaseModel
from tortoise.contrib.pydantic import pydantic_model_creator

class User(Model):
    id = fields.IntField(primary_key=True)
    username = fields.CharField(max_length=16, unique = True)
    hashed_password = fields.CharField(max_length=22)
    email = fields.CharField(max_length=255, unique = True)
    is_verified = fields.BooleanField()
    profile_picture = fields.CharField(max_length = 255, null = True)
    is_admin = fields.BooleanField()
    created_at = fields.DatetimeField(auto_now_add=True)
    updated_at = fields.DatetimeField(auto_now=True)
    reset_token = fields.CharField(max_length=255, null = True)
    reset_token_expiry = fields.DatetimeField(null = True)

    class Meta:
        table = "users"

user_pydantic = pydantic_model_creator(User, name = "User", exclude=("is_verified", ))
user_pydanticIn = pydantic_model_creator(User, name = "UserIn", exclude_readonly=True)
user_pydanticOut = pydantic_model_creator(User, name = "UserOut", exclude = ("password", ))
