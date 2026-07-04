import json

from app.llm.client import ask_llm
from app.llm.prompts import INTENT_SYSTEM_PROMPT


class IntentAgent:

    def process(self, intent: str):

        response = ask_llm(
            INTENT_SYSTEM_PROMPT,
            intent
        )

        return json.loads(response)