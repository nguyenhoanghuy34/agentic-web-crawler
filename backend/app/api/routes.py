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