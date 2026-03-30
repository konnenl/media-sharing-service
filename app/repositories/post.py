from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from app.models.post import Post
from uuid import uuid4

class PostRepository:
    def __init__(self, session: AsyncSession):
        self.session = session

    async def create(self, url: str, file_type: str, file_name: str, caption: str | None = None) -> Post:
        post = Post(
            id=uuid4(),
            url=url,
            file_type=file_type,
            file_name=file_name,
            caption=caption
        )
        self.session.add(post)
        await self.session.commit()
        await self.session.refresh(post)
        return post

    async def get_all(self) -> list[Post]:
        res = await self.session.execute(select(Post).order_by(Post.created_at.desc()))
        return res.scalars().all()