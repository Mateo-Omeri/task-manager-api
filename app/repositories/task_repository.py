from sqlalchemy.orm import Session
from app.models.task import Task
from app.schemas.task import TaskCreate, TaskUpdate


class TaskRepository:

    def __init__(self, db: Session):
        self.db = db

    def create(self, schema: TaskCreate) -> Task:
        task = Task(**schema.model_dump())
        self.db.add(task)
        self.db.commit()
        self.db.refresh(task)
        return task

    def get_all(self) -> list[Task]:
        return self.db.query(Task).all()

    def get_by_id(self, task_id: str) -> Task | None:
        return self.db.query(Task).filter(Task.id == task_id).first()

    def update(self, task_id: str, schema: TaskUpdate) -> Task | None:
        task = self.get_by_id(task_id)
        if not task:
            return None
        for key, value in schema.model_dump(exclude_unset=True).items():
            setattr(task, key, value)
        self.db.commit()
        self.db.refresh(task)
        return task

    def delete(self, task_id: str) -> bool:
        task = self.get_by_id(task_id)
        if not task:
            return False
        self.db.delete(task)
        self.db.commit()
        return True
