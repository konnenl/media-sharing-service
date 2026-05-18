from fastapi import APIRouter, Depends, HTTPException

from app.auth.dependencies import fastapi_users, get_user_manager, current_user
from app.auth.backend import auth_backend
from app.schemas.user import *


router = APIRouter(prefix="/auth", tags=["auth"])

router.include_router(fastapi_users.get_auth_router(auth_backend), prefix="/jwt", tags=["auth"])
router.include_router(fastapi_users.get_register_router(UserRead, UserCreate), tags=["auth"])
router.include_router(fastapi_users.get_users_router(UserRead, UserUpdate), prefix="/users", tags=["users"])