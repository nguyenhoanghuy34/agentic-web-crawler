from fastapi import FastAPI
from app.api.routes import router
from app.core.init_db import init_db

app = FastAPI(title="Agentic Web Crawler")

app.include_router(router)


@app.on_event("startup")
async def startup():

    await init_db()