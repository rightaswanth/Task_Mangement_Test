from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession, async_sessionmaker
from sqlalchemy.orm import DeclarativeBase

from settings import settings


engine = create_async_engine(settings.database_url, echo=False)

async_session_maker = async_sessionmaker(
    engine,
    class_=AsyncSession,
    autocommit=False,
    autoflush=False,
    expire_on_commit=False
)


class Base(DeclarativeBase):
    pass


async def get_db():
    async with async_session_maker() as session:
        yield session