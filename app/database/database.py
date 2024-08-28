import os
from sqlalchemy.ext.asyncio.session import AsyncSession
from sqlalchemy.orm import DeclarativeBase
from sqlalchemy.ext.asyncio import create_async_engine, async_sessionmaker, AsyncAttrs
from sqlalchemy.exc import SQLAlchemyError
from typing import AsyncGenerator


class Base(AsyncAttrs, DeclarativeBase):  # !
    pass


DATABASE_URL = (f'postgresql+asyncpg2://{os.environ.get("DB_USERNAME")}:'
                f'{os.environ.get("DB_PASSWORD")}@{os.environ.get("DB_HOST")}'
                f':5432/{os.environ.get("DB_NAME")}')

engine = create_async_engine(DATABASE_URL, echo=True)
session = async_sessionmaker(engine)


async def async_get_db() -> AsyncGenerator[AsyncSession, None]:
    async_session = session
    async with async_session() as db:
        try:
            yield db
            await db.commit()
        except SQLAlchemyError:
            await db.rollback()
