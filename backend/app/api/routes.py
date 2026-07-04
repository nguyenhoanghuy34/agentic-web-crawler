from fastapi import APIRouter
from app.api.schemas import CrawlRequest, CrawlResponse
from app.services.pipeline_service import PipelineService

router = APIRouter()

pipeline = PipelineService()


@router.post("/crawl", response_model=CrawlResponse)
async def crawl(req: CrawlRequest):
    job_id = await pipeline.run(req)
    return {"job_id": job_id, "status": "processing"}