import uuid


class JobManager:

    def __init__(self):

        self.jobs = {}

    def create(self):

        job_id = str(uuid.uuid4())

        self.jobs[job_id] = {

            "status": "created"

        }

        return job_id

    def update(self, job_id, data):

        self.jobs[job_id].update(data)

    def get(self, job_id):

        return self.jobs.get(job_id)