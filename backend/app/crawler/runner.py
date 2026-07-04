from scrapy.crawler import CrawlerProcess
from scrapy.utils.project import get_project_settings

from app.crawler.spiders.generic_spider import GenericSpider


def run_crawler(urls: list):

    settings = get_project_settings()

    process = CrawlerProcess(settings)

    collected_data = []

    def collect(item):
        collected_data.append(item)

    process.crawl(GenericSpider, urls=urls)

    for spider in process.crawlers:

        spider.signals.connect(collect, signal="item_scraped")

    process.start()

    return collected_data