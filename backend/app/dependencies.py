from app.services.pipeline_service import PipelineService
from app.core.database import get_db

pipeline = PipelineService()


def get_db_session():
    return get_db()