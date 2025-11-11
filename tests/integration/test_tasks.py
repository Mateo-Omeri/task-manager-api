def generate_payload():
    return {
        "title": "Test Task",
        "description": "This is a test task",
        "completed": False,
    }


def test_get_tasks_initially_empty(client):
    resp = client.get("/api/tasks")
    assert resp.status_code == 200
    assert resp.json() == []


def test_post_task_creates_task(client):
    payload = generate_payload()
    resp = client.post("/api/tasks", json=payload)
    assert resp.status_code == 201 or resp.status_code == 200
    data = resp.json()
    assert data["title"] == payload["title"]
    assert "id" in data


def test_get_task_by_id(client):
    payload = generate_payload()
    post = client.post("/api/tasks", json=payload)
    task = post.json()
    resp = client.get(f"/api/tasks/{task['id']}")
    assert resp.status_code == 200
    assert resp.json()["id"] == task["id"]


def test_put_task_updates_task(client):
    payload = generate_payload()
    post = client.post("/api/tasks", json=payload)
    task = post.json()
    update = {"title": "Updated Title", "completed": True}
    resp = client.put(f"/api/tasks/{task['id']}", json=update)
    assert resp.status_code == 200
    data = resp.json()
    assert data["title"] == "Updated Title"
    assert data["completed"] is True


def test_delete_task(client):
    payload = generate_payload()
    post = client.post("/api/tasks", json=payload)
    task = post.json()
    resp = client.delete(f"/api/tasks/{task['id']}")
    assert resp.status_code in (200, 204)
    # verify not found after delete
    resp2 = client.get(f"/api/tasks/{task['id']}")
    assert resp2.status_code == 404


def test_get_by_id_not_found(db_session):
    from app.repositories.task_repository import TaskRepository

    repo = TaskRepository(db_session)
    result = repo.get_by_id(999)
    assert result is None


def test_update_not_found(db_session):
    from app.repositories.task_repository import TaskRepository
    from app.schemas.task import TaskUpdate

    repo = TaskRepository(db_session)
    result = repo.update(999, TaskUpdate(title="x"))
    assert result is None


def test_delete_not_found(db_session):
    from app.repositories.task_repository import TaskRepository

    repo = TaskRepository(db_session)
    result = repo.delete(999)
    assert result is False
