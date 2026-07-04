from app.crawler.runner import run_crawler


class CrawlService:

    def run(self, urls: list):

        return run_crawler(urls)