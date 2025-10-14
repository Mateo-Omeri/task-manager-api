from fastapi import APIRouter, HTTPException
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

@router.get("/{task_id}", response_model=Task)
async def get_task_by_id(task_id: str):
    for task in tasks:
        if task.id == task_id:
            return task
    raise HTTPException(status_code=404, detail="Task not found")

@router.put("/{task_id}", response_model=Task)
async def update_task(task_id: str, updated_task: Task):
    for index, task in enumerate(tasks):
        if task.id == task_id:
            tasks[index] = updated_task
            return updated_task
    raise HTTPException(status_code=404, detail="Task not found")

@router.delete("/{task_id}")
async def delete_task(task_id: str):
    for index, task in enumerate(tasks):
        if task.id == task_id:
            del tasks[index]
            return [{"status": "deleted"}]
    raise HTTPException(status_code=404, detail="Task not found")