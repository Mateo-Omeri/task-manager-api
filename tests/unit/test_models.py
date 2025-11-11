from app.models.task import Task


def test_task_model_defaults():
    t = Task(title="hello")
    assert t.title == "hello"
    assert hasattr(t, "id")
    assert t.completed is None or False
