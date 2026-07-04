class CrawlConfigAgent:

    def run(self, urls: list):

        return {

            "delay": 2,

            "concurrency": 2,

            "respect_robots": True,

            "retry": True,

            "headers": {

                "User-Agent": "Mozilla"

            }

        }