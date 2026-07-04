from langchain_openai import ChatOpenAI

from app.core.config import settings


def get_llm():

    return ChatOpenAI(

        model=settings.MODEL_NAME,

        api_key=settings.OPENAI_API_KEY,

        temperature=0.2

    )