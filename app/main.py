from fastapi import FastAPI
from app.routers import health, tasks

app = FastAPI(title = 'Todo API')

app.include_router(health.router, prefix = "/api")
app.include_router(tasks.router, prefix = "/api")

@app.get("/")
async def root():
    return {"message": "Welcome to the Todo API!"}