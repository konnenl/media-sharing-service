from imagekitio import ImageKit
from app.core.config import IMAGEKIT_PRIVATE_KEY

imagekit = ImageKit(
    private_key=IMAGEKIT_PRIVATE_KEY,
)