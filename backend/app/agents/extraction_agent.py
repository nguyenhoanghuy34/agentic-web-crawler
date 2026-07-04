import json

from app.llm.client import ask_llm
from app.llm.prompts import EXTRACTION_SYSTEM_PROMPT


class ExtractionAgent:

    def process(self, raw_data, user_prompt):

        prompt = f"""
User Request:

{user_prompt}

Scraped Data:

{raw_data}
"""

        response = ask_llm(
            EXTRACTION_SYSTEM_PROMPT,
            prompt
        )

        return json.loads(response)