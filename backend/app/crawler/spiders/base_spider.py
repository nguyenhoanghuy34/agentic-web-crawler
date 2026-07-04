import scrapy


class BaseSpider(scrapy.Spider):
    name = "base"

    def parse(self, response):
        yield {
            "url": response.url,
            "title": response.css("title::text").get(),
            "text": " ".join(response.css("p::text").getall())[:500]
        }