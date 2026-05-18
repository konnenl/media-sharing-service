from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from app.models.post import Post
from uuid import uuid4, UUID
from sqlalchemy.exc import SQLAlchemyError

class PostRepository:
    def __init__(self, session: AsyncSession):
        self.session = session

    async def create(self, url: str, file_type: str, file_name: str, user_id: UUID, caption: str | None = None) -> Post:
        post = Post(
            id=uuid4(),
            user_id=user_id,
            url=url,
            file_type=file_type,
            file_name=file_name,
            caption=caption
        )
        self.session.add(post)
        try:
            await self.session.commit()
            await self.session.refresh(post)
        except SQLAlchemyError:
            await self.session.rollback()
            raise

        return post

    async def get_all(self) -> list[Post]:
        res = await self.session.execute(select(Post).order_by(Post.created_at.desc()))
        return res.scalars().all()
    
    async def delete(self, post: Post) -> None:
        await self.session.delete(post)
        await self.session.commit()
    
    async def get_by_id(self, post_uuid: UUID) -> Post | None:
        res = await self.session.execute(select(Post).where(Post.id == post_uuid))
        return res.scalar_one_or_none()