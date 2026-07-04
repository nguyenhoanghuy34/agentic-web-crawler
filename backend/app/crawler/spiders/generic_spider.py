from app.crawler.spiders.base_spider import BaseSpider


class GenericSpider(BaseSpider):
    name = "generic"

    def __init__(self, urls=None, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.start_urls = urls or []