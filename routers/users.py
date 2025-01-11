from fastapi import APIRouter
from tortoise.models import Model
router = APIRouter

@router.get("users/", tags=["users"])
async def read_users():
    return 