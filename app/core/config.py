import os
from dotenv import load_dotenv

load_dotenv()

DATABASE_URL = os.getenv("DATABASE_URL")
SYNC_DATABASE_URL = os.getenv("SYNC_DATABASE_URL")

IMAGEKIT_PRIVATE_KEY = os.getenv("IMAGEKIT_PRIVATE_KEY")
IMAGEKIT_PUBLIC_KEY = os.getenv("IMAGEKIT_PUBLIC_KEY")
IMAGEKIT_URL = os.getenv("IMAGEKIT_URL")

JWT_SECRET = os.getenv("JWT_SECRET")