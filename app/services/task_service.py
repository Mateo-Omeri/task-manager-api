from app.repositories.task_repository import TaskRepository
from app.schemas.task import TaskCreate, TaskUpdate


class TaskService:
    def __init__(self, repo: TaskRepository):
        self.repo = repo

    def list_tasks(self):
        return self.repo.get_all()

    def create_task(self, task: TaskCreate):
        return self.repo.create(task)

    def get_task_by_id(self, task_id: int):
        return self.repo.get_by_id(task_id)

    def update_task(self, task_id: int, task: TaskUpdate):
        return self.repo.update(task_id, task)

    def delete_task(self, task_id: int):
        return self.repo.delete(task_id)
