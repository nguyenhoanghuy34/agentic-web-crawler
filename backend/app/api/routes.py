from fastapi import APIRouter

from app.dependencies import pipeline

from app.api.schemas import *

router = APIRouter()


@router.post("/crawl")

async def crawl(req: CrawlRequest):

    job = await pipeline.run(req)

    return {

        "job_id": job,

        "status": "running"

    }

@router.post("/users")
async def create_user(email: str, password: str, db: AsyncSession = Depends(get_db)):

    user = User(email=email, password=password)

    db.add(user)

    await db.commit()

    return {"status": "created"}

