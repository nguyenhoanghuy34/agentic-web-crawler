from fastapi import FastAPI

from app.api.routes import router

app = FastAPI(
    title="Agentic Web Crawler"
)

app.include_router(router)