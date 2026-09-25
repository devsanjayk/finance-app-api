from fastapi import FastAPI
from app.api.routes import health

app  = FastAPI(
    title="Finance app",
    description="Backend API for the application",
    version="0.1.0",
)

app.include_router(health.router)