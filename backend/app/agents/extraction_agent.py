from langchain_core.prompts import ChatPromptTemplate

from langchain_core.output_parsers import JsonOutputParser

from app.llm.factory import get_llm

from app.llm.prompts import EXTRACTION_PROMPT


class ExtractionAgent:

    def __init__(self):

        self.llm = get_llm()

        self.parser = JsonOutputParser()

    def run(

        self,

        raw_data,

        user_prompt

    ):

        prompt = ChatPromptTemplate.from_messages(

            [

                ("system", EXTRACTION_PROMPT),

                (

                    "human",

                    """

User Request

{prompt}

Scraped Data

{data}

"""

                )

            ]

        )

        chain = prompt | self.llm | self.parser

        return chain.invoke(

            {

                "prompt": user_prompt,

                "data": raw_data

            }

        )