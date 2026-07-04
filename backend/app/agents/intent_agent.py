import json

from langchain_core.output_parsers import JsonOutputParser

from langchain_core.prompts import ChatPromptTemplate

from app.llm.factory import get_llm

from app.llm.prompts import INTENT_PROMPT


class IntentAgent:

    def __init__(self):

        self.llm = get_llm()

        self.parser = JsonOutputParser()

    def run(self, intent: str):

        prompt = ChatPromptTemplate.from_messages(

            [

                ("system", INTENT_PROMPT),

                ("human", "{intent}")

            ]

        )

        chain = prompt | self.llm | self.parser

        return chain.invoke(

            {

                "intent": intent

            }

        )