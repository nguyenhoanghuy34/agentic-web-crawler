import random


class UserAgentMiddleware:

    USER_AGENTS = [

        "Mozilla/5.0 (Windows NT 10.0; Win64; x64)",

        "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7)",

        "Mozilla/5.0 (X11; Linux x86_64)",

        "Mozilla/5.0 (iPhone; CPU iPhone OS 14_0 like Mac OS X)"

    ]

    def process_request(self, request, spider):

        request.headers["User-Agent"] = random.choice(self.USER_AGENTS)


class RetryMiddleware:

    def process_response(self, request, response, spider):

        if response.status in [403, 429, 500]:

            spider.logger.warning(

                f"Retry triggered: {response.status} | {request.url}"

            )

            return request  # retry lại request

        return response