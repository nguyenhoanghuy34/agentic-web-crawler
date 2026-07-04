class ExtractionAgent:

    def process(self, raw_data, user_prompt: str):
        results = []

        for item in raw_data:
            results.append({
                "name": item.get("title"),
                "price": item.get("price"),
                "website": item.get("url"),
                "description": item.get("description"),
                "category": "unknown"
            })

        return {"results": results}