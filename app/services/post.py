from sqlalchemy.ext.asyncio import AsyncSession
from app.repositories.post import PostRepository
from app.schemas.post import PostCreate
from app.clients.imagekit import imagekit
import uuid
from app.core.exceptions import *

class PostService:
    def __init__(self, session: AsyncSession):
        self.repo = PostRepository(session)
    
    async def create_post(self, post_data: PostCreate, user_id):
        file = post_data.file

        try:
            upload_res = imagekit.files.upload(
                file=file.file,
                file_name=file.filename,
                use_unique_file_name=True,
                tags=["backend-upload"]
            )
        except Exception as e:
            raise ExternalServiceError("imagekit", message=str(e))
        finally:
            file.file.close()
        
        file_type = "video" if file.content_type.startswith("video/") else "image"
        return await self.repo.create(
            user_id=user_id,
            url=upload_res.url,
            file_type=file_type,
            file_name=upload_res.name,
            caption=post_data.caption
        )
    
    async def get_feed(self):
        return await self.repo.get_all()
    
    async def delete(self, post_id: str, user_id):
        try:
            post_uuid = uuid.UUID(post_id)
        except ValueError:
            raise ValidationError("post_id", "Invalid UUID", post_id)

        post = await self.repo.get_by_id(post_uuid)
        
        if not post:
            raise NotFoundError("Post", post_id)
        
        if post.user_id != user_id:
            raise ForbiddenError("You can't delete this post")

        await self.repo.delete(post)