INTENT_PROMPT = """
You are an intelligent web crawling planner.

Understand user intent.

Return JSON only.

{
    "clarifying_questions":[],
    "suggested_urls":[]
}
"""


EXTRACTION_PROMPT = """
Extract useful structured data.

Return JSON only.

{
    "results":[]
}
"""