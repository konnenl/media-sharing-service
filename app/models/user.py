from sqlalchemy.orm import relationship
from fastapi_users.db import SQLAlchemyBaseUserTableUUID

from app.db.database import Base

class User(SQLAlchemyBaseUserTableUUID, Base):
    __tablename__ = "users"

    posts = relationship("Post", back_populates="user")