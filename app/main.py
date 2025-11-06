from fastapi import FastAPI

from app.core.error_handlers import setup_exception_handlers
from app.core.logging_config import configure_logging
from app.routers import health, tasks

configure_logging()

app = FastAPI(title="Todo API")

setup_exception_handlers(app)

app.include_router(health.router, prefix="/api")
app.include_router(tasks.router, prefix="/api")


@app.get("/")
async def root():
    return {"message": "Welcome to the Todo API!"}
