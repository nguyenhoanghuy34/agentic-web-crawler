from pydantic import BaseModel
from typing import List


class CrawlRequest(BaseModel):

    mode: str

    intent: str | None = None

    urls: List[str] | None = None


class CrawlResponse(BaseModel):

    job_id: str

    status: str