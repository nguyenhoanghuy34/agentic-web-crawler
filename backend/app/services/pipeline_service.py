from app.core.job_manager import JobManager
from app.agents.intent_agent import IntentAgent
from app.agents.crawl_config_agent import CrawlConfigAgent
from app.agents.extraction_agent import ExtractionAgent
from app.crawler.runner import ScrapyRunner
from app.utils.excel_export import export_excel


class PipelineService:

    def __init__(self):
        self.job_manager = JobManager()
        self.intent_agent = IntentAgent()
        self.config_agent = CrawlConfigAgent()
        self.extract_agent = ExtractionAgent()
        self.crawler = ScrapyRunner()

    async def run(self, req):

        job_id = self.job_manager.create_job()
        self.job_manager.update(job_id, {"status": "intent_processing"})

        # STEP 1: intent resolve
        if req.mode == "intent":
            intent_result = self.intent_agent.process(req.intent)
            urls = intent_result["suggested_urls"]
        else:
            urls = req.urls

        # STEP 2: crawl config
        config = self.config_agent.generate(urls)

        self.job_manager.update(job_id, {"status": "crawling"})

        # STEP 3: crawl
        raw_data = await self.crawler.run(urls, config)

        # STEP 4: extract
        self.job_manager.update(job_id, {"status": "processing"})

        processed = self.extract_agent.process(raw_data, req.intent or "")

        # STEP 5: export
        file_path = export_excel(job_id, processed["results"])

        self.job_manager.update(job_id, {
            "status": "done",
            "file": file_path,
            "result": processed
        })

        return job_id