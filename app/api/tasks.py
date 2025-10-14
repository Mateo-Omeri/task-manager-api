from fastapi import APIRouter
from app.models.task import Task
from typing import List

router = APIRouter(tags = ["tasks"])

#temporary in-memory storge
tasks: list[Task] = []

@router.get("/tasks", response_model=List[Task])
async def get_all_tasks():
    return tasks