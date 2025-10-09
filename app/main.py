from fastapi import FastAPI
from .api import health

app = FastAPI(title = 'Todo API')

app.include_router(health.router, prefix = "/api/v1")

@app.get("/")
async def root():
    return {"message": "Welcome to the Todo API!"}