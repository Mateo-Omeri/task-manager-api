import uuid

from fastapi.testclient import TestClient

from app.main import app

client = TestClient(app)


def generate_task():
    return {
        "id": str(uuid.uuid4()),
        "title": "Test Task",
        "description": "This is a test task",
        "completed": False,
    }


def test_get_tasks_initially_empty():
    response = client.get("/api/tasks")
    assert response.status_code == 200
    assert response.json() == []


def test_post_task_creates_task():
    task_data = generate_task()
    response = client.post("/api/tasks", json=task_data)
    assert response.status_code == 200
    assert response.json() == task_data


def test_get_task_by_id():
    task_data = generate_task()
    client.post("/api/tasks", json=task_data)
    response = client.get(f"/api/tasks/{task_data['id']}")
    assert response.status_code == 200
    assert response.json() == task_data


def test_get_task_not_found():
    response = client.get("/api/tasks/nonexistent-id")
    assert response.status_code == 404


def test_put_task_updates_task():
    task_data = generate_task()
    client.post("/api/tasks", json=task_data)
    updated_data = task_data.copy()
    updated_data["title"] = "Updated Title"
    updated_data["completed"] = True
    response = client.put(f"/api/tasks/{task_data['id']}", json=updated_data)
    assert response.status_code == 200
    assert response.json()["title"] == "Updated Title"
    assert response.json()["completed"] is True


def test_delete_task():
    task_data = generate_task()
    client.post("/api/tasks", json=task_data)
    response = client.delete(f"/api/tasks/{task_data['id']}")
    assert response.status_code == 200
    assert response.json() == [{"status": "deleted"}]


def test_delete_task_not_found():
    response = client.delete("/api/tasks/nonexistent-id")
    assert response.status_code == 404
