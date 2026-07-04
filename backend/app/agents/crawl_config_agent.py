class CrawlConfigAgent:

    def generate(self, urls: list):
        return {
            "crawl_config": {
                "delay": 2,
                "concurrency": 2,
                "respect_robots": True,
                "retry": True,
                "user_agent": "Mozilla/5.0 MockBot"
            },
            "urls": urls
        }