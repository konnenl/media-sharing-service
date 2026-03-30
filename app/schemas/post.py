from pydantic import BaseModel
from typing import Optional
from uuid import UUID
from datetime import datetime

class PostCreate(BaseModel):
    caption: Optional[str] = ""
    url: str
    file_type: str
    file_name: str

class PostResponse(BaseModel):
    id: UUID
    caption: Optional[str]
    url: str
    file_type: str
    file_name: str
    created_at: datetime

    class Config:
        orm_mode = True