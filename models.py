from tortoise.models import Model
from tortoise import fields
from datetime import datetime
from pydantic import BaseModel

class User(Model):
    id = fields.IntField(primary_key=True)
    username = fields.CharField(max_length=16, unique = True)
    hashed_password = fields.CharField(max_length=22)
    email = fields.CharField(max_length=255, unique = True)
    is_verified = fields.BooleanField()
    profile_picture = fields.CharField(max_length = 255, null = True)
    is_admin = fields.BooleanField()
    created_at = fields.CharField(auto_now_add=True)
    updated_at = fields.DatetimeField(auto_now=True)
    reset_token = fields.CharField(max_length=255, null = True)
    reset_token_expiry = fields.DatetimeField(null = True)

    class Meta:
        table = "users"
