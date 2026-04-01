from fastapi import APIRouter, HTTPException, File, UploadFile, Form, Depends
from app.schemas.post import PostCreate, PostResponse
from sqlalchemy.ext.asyncio import AsyncSession
from app.db.database import get_async_session
from app.services.post import PostService


router = APIRouter(prefix="/posts", tags=["posts"])

@router.post("/upload", response_model=PostResponse)
async def upload_file(
    file: UploadFile = File(...),
    caption: str = Form(""),
    session: AsyncSession = Depends(get_async_session)
):
    post_data = PostCreate(
        file=file,
        caption=caption
    )
    service = PostService(session)
    try:
        post = await service.create_post(post_data)
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))
    return post


@router.get("/feed", response_model=list[PostResponse])
async def get_feed(
    session: AsyncSession = Depends(get_async_session)
):
    service = PostService(session)
    posts = await service.get_feed()
    return posts