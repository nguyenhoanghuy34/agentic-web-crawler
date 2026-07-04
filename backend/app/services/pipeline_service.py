from app.core.job_manager import JobManager

from app.graph.graph import graph


class PipelineService:

    def __init__(self):

        self.job_manager = JobManager()

    async def run(self, req):

        job_id = self.job_manager.create()

        state = {

            "job_id": job_id,

            "mode": req.mode,

            "intent": req.intent or "",

            "urls": req.urls or [],

            "crawl_config": {},

            "raw_data": [],

            "processed_data": []

        }

        result = graph.invoke(state)

        self.job_manager.update(job_id, {

            "status": "done",

            "result": result

        })

        return job_id