class IntentAgent:

    def process(self, intent: str):
        # mock logic
        if not intent:
            return {
                "clarifying_questions": ["Bạn muốn phân tích ngành nào?"],
                "suggested_urls": [],
                "urls": []
            }

        return {
            "clarifying_questions": [],
            "suggested_urls": [
                "https://shopee.vn",
                "https://tiki.vn",
                "https://lazada.vn"
            ],
            "urls": []
        }