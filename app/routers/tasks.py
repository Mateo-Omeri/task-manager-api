from fastapi import APIRouter, Depends, HTTPException, status
from app.db import get_db
from app.repositories.task_repository import TaskRepository
from app.schemas.task import TaskCreate, TaskUpdate, TaskResponse

router = APIRouter(prefix = "/tasks", tags = ["tasks"])

def get_task_repo(db=Depends(get_db)):
    return TaskRepository(db)

@router.get("/tasks", response_model=list[TaskResponse])
def list_tasks(repo: TaskRepository = Depends(get_task_repo)):
    return repo.get_all()

@router.post("/", response_model=TaskResponse, status_code=status.HTTP_201_CREATED)
def create_task(task: TaskCreate, repo: TaskRepository = Depends(get_task_repo)):
    return repo.create(task)

@router.get("/{task_id}", response_model=TaskResponse)
def get_task(task_id: int, repo: TaskRepository = Depends(get_task_repo)):
    task = repo.get_by_id(task_id)
    if not task:
        raise HTTPException(status_code=404, detail="Task not found")
    return task

@router.put("/{task_id}", response_model=TaskResponse)
def update_task(task_id: int, task: TaskUpdate, repo: TaskRepository = Depends(get_task_repo)):
    updated = repo.update(task_id, task)
    if not updated:
        raise HTTPException(status_code=404, detail="Task not found")
    return updated

@router.delete("/{task_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_task(task_id: int, repo: TaskRepository = Depends(get_task_repo)):
    deleted = repo.delete(task_id)
    if not deleted:
        raise HTTPException(status_code=404, detail="Task not found")