from fastapi_users import BaseUserManager, UUIDIDMixin
from uuid import UUID
from fastapi import Depends

from app.models.user import User
from app.core.config import JWT_SECRET
from app.db.users import get_user_db

class UserManager(UUIDIDMixin, BaseUserManager[User, UUID]):
    reset_password_token_secret = JWT_SECRET
    verification_token_secret = JWT_SECRET

async def get_user_manager(user_db=Depends(get_user_db)):
    yield UserManager(user_db)