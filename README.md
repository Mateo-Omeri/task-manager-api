# 📝 To-Do List API
![CI](https://github.com/Mateo-Omeri/task-manager-api/actions/workflows/ci.yml/badge.svg)

A minimal yet production-oriented REST API for task management, designed to practice software engineering fundamentals such as:

- layered architecture  
- separation of concerns  
- automated testing  
- continuous integration  
- containerization  

The domain (to-do tasks) is intentionally simple, while the engineering practices mirror real-world backend systems.

---

## 🚀 Overview

The API exposes CRUD endpoints to manage tasks:

- create tasks  
- list tasks  
- update tasks  
- delete tasks  

Although functionally simple, the project is structured as if it were a production service, with attention to:

- explicit architectural layers  
- testability  
- reproducible environments  
- CI enforcement  
- progressive refactoring

---

## 🧩 Tech Stack

| Category              | Technology                          |
|-----------------------|-------------------------------------|
| Language              | Python 3.12                         |
| Web framework         | FastAPI                             |
| ORM                   | SQLAlchemy                          |
| Data validation       | Pydantic                            |
| Database              | SQLite (default) / PostgreSQL (Docker Compose) |
| Testing               | pytest                              |
| Linting & formatting  | ruff, black, isort, pre-commit      |
| Containerization      | Docker                              |
| CI                    | GitHub Actions                      |

---

## 🏗️ Architecture

The application follows a layered architecture:

```text
app/
 ├── main.py            # FastAPI application entrypoint
 ├── routers/           # HTTP layer (request/response handling)
 ├── services/          # Business logic layer (optional / extensible)
 ├── repositories/      # Persistence layer (DB access)
 ├── models/            # SQLAlchemy ORM models
 ├── schemas/           # Pydantic DTOs
 ├── core/              # Cross-cutting concerns (logging, errors)
 └── db.py              # Database configuration and session management
```
### Layer Responsibilities

#### Routers
- Define HTTP endpoints  
- Perform request validation through schemas  
- Delegate logic to repositories/services  
- Map domain errors to HTTP responses  

#### Repositories
- Encapsulate all database interactions  
- Provide CRUD operations  
- Abstract SQLAlchemy session usage from higher layers  

#### Schemas (Pydantic)
- Define request/response contracts  
- Enforce validation and serialization  

#### Models (SQLAlchemy)
- Represent persistent entities  
- Map directly to database tables  

#### Core
- Centralized logging configuration  
- Global exception handlers for consistent error responses  

#### DB Module
- Manages SQLAlchemy engine and sessions  
- Supports dynamic backend selection (SQLite vs PostgreSQL via env var)  

This structure ensures:

- loose coupling between HTTP and persistence layers  
- easier refactoring  
- improved testability  
- clear ownership of responsibilities

---

## 🧪 Testing Strategy

Tests are split by scope:

```text
tests/
 ├── unit/          # Isolated behavior tests
 └── integration/   # Full API tests with real DB session
```
### Unit Tests
- model defaults  
- error handlers  
- health endpoint  
- pure logic behavior  

### Integration Tests
- use a temporary SQLite database  
- exercise full request lifecycle:  
  - POST → GET → PUT → DELETE  
- validate:
  - HTTP status codes  
  - response schemas  
  - persistence correctness  

The integration tests override the application DB dependency to ensure isolation.

**Current coverage: ~90%+**

---

## ⚠️ Design Trade-offs

| Decision          | Rationale                              |
|-------------------|----------------------------------------|
| SQLite by default | Zero configuration for local dev       |
| No authentication | Focus on architecture and tooling      |
| Simple domain     | Emphasis on engineering practices      |
| No migrations yet | Avoid premature complexity             |
| FastAPI           | Rapid development + automatic OpenAPI docs |

The project prioritizes engineering correctness over feature richness.

---

## ⚙️ Installation

```bash
git clone https://github.com/Mateo-Omeri/task-manager-api.git
cd task-manager-api
pip install -r requirements.txt
```

---

## ▶️ Run locally

```bash
uvicorn app.main:app --reload
```

Health check:
```http
GET http://127.0.0.1:8000/api/health
```

Response:
```json
{"status": "ok"}
```

---

## ▶️ Run tests

```bash
pytest
```

---

## 🐳 Docker

Build image:

```bash
docker build -t todo-api .
```

Run container:
```bash
docker run -p 8000:8000 todo-api
```
The application uses SQLite by default.

---

## 🔄 Continuous Integration

A GitHub Actions workflow runs on:

- every push  
- every pull request  

Pipeline steps:

1. Setup Python  
2. Install dependencies  
3. Run linters & formatters  
4. Execute test suite  

This guarantees:

- code quality enforcement  
- test correctness  
- stable main branch  

---

## 🎯 Learning Objectives

This project was built to practice:

- API design  
- layered architecture  
- automated testing  
- CI pipelines  
- Dockerization  
- safe refactoring  

It serves as a technical foundation for future projects in:

- backend systems  
- ETL services  
- data ingestion pipelines  

---

## 📌 Status

**Completed:**
- CRUD API  
- layered structure  
- logging  
- tests  
- CI  
- Docker  

**Optional future extensions:**
- PostgreSQL  
- Alembic migrations  
- deployment

---