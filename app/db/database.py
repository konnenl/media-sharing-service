from collections.abc import AsyncGenerator
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.ext.asyncio import AsyncSession, create_async_engine, async_sessionmaker
from app.core.config import DATABASE_URL, SYNC_DATABASE_URL
from sqlalchemy import create_engine
from sqlalchemy.ext.asyncio import AsyncSession

Base = declarative_base()
async_engine = create_async_engine(DATABASE_URL)
async_session_maker = async_sessionmaker(async_engine, expire_on_commit=False)

sync_engine = create_engine(SYNC_DATABASE_URL)

async def get_async_session() -> AsyncGenerator[AsyncSession, None]:
    async with async_session_maker() as session:
        yield session