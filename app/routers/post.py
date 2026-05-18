from fastapi import APIRouter, HTTPException, File, UploadFile, Form, Depends
from app.schemas.post import PostCreate, PostResponse
from sqlalchemy.ext.asyncio import AsyncSession

from app.db.database import get_async_session
from app.auth.dependencies import current_user
from app.models.user import User
from app.services.post import PostService

router = APIRouter(prefix="/posts", tags=["posts"])

@router.post("/upload", response_model=PostResponse)
async def upload_file(
    file: UploadFile = File(...),
    caption: str = Form(""),
    session: AsyncSession = Depends(get_async_session),
    user: User = Depends(current_user)
):
    post_data = PostCreate(file=file, caption=caption)
    service = PostService(session)
    post = await service.create_post(post_data, user_id=user.id)
    return post


@router.get("/feed", response_model=list[PostResponse])
async def get_feed(
    session: AsyncSession = Depends(get_async_session)
):
    service = PostService(session)
    posts = await service.get_feed()
    return posts

@router.delete("/delete/{post_id}")
async def delete_post(
    post_id: str,
    session: AsyncSession = Depends(get_async_session),
    user: User = Depends(current_user)
):
    service = PostService(session)
    await service.delete(post_id, user.id)
    return {"status": "ok"}