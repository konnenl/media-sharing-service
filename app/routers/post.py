from fastapi import APIRouter, HTTPException, File, UploadFile, Form, Depends
from app.schemas.post import PostCreate, PostResponse
from sqlalchemy.ext.asyncio import AsyncSession
from app.db.database import get_async_session
from app.services.post import PostService
from app.core.exceptions import PostNotFoundError, InvalidPostIdError

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

@router.delete("/delete/{post_id}")
async def delete_post(
    post_id: str,
    session: AsyncSession = Depends(get_async_session)
):
    service = PostService(session)
    try:
        await service.delete(post_id)
        return {"status": "ok"}
    except InvalidPostIdError as e:
        raise HTTPException(status_code=400, detail=str(e))
    except PostNotFoundError as e:
        raise HTTPException(status_code=404, detail=str(e))
    except Exception as e:
        print(e)
        raise HTTPException(status_code=500, detail="Internal server error")