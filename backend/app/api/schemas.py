from pydantic import BaseModel
from typing import List, Optional


class CrawlRequest(BaseModel):
    mode: str  # "intent" or "urls"
    intent: Optional[str] = None
    urls: Optional[List[str]] = None


class CrawlResponse(BaseModel):
    job_id: str
    status: str