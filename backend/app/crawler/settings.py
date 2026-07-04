BOT_NAME = "agent_crawler"

ROBOTSTXT_OBEY = False

DOWNLOAD_DELAY = 1

CONCURRENT_REQUESTS = 4

USER_AGENT = "Mozilla/5.0 (compatible; AgentCrawler/1.0)"

RETRY_ENABLED = True

DOWNLOADER_MIDDLEWARES = {

    "app.crawler.middlewares.UserAgentMiddleware": 400,

    "app.crawler.middlewares.RetryMiddleware": 500,

}