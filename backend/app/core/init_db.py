from app.core.database import engine
from app.core.base import Base

from app.models.user import User
from app.models.job import Job


async def init_db():

    async with engine.begin() as conn:

        await conn.run_sync(Base.metadata.create_all)