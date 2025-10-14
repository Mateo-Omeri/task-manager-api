from fastapi import APIRouter
from app.models.task import Task
from typing import List

router = APIRouter(prefix = "/tasks", tags = ["tasks"])

#temporary in-memory storge
tasks: list[Task] = []

@router.get("/", response_model=List[Task])
async def get_all_tasks():
    return tasks

@router.post("/", response_model=Task)
async def create_task(task: Task):
    tasks.append(task)
    return task