from sqlalchemy.ext.asyncio import AsyncSession
from app.repositories.post import PostRepository
from app.schemas.post import PostCreate

class PostService:
    def __init__(self, session: AsyncSession):
        self.repo = PostRepository(session)
    
    async def create_post(self, post_data: PostCreate):
        return await self.repo.create(
            url=post_data.url,
            file_type=post_data.file_type,
            file_name=post_data.file_name,
            caption=post_data.caption
        )
    
    async def get_feed(self):
        return await self.repo.get_all()