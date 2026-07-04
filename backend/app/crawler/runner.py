import asyncio


class ScrapyRunner:

    async def run(self, urls, config):
        # MOCK scrapy run (sau này thay bằng scrapy crawl)
        results = []

        for url in urls:
            await asyncio.sleep(config["crawl_config"]["delay"])

            results.append({
                "url": url,
                "title": f"Fake data from {url}",
                "price": "100$",
                "description": "mock scraped content"
            })

        return results