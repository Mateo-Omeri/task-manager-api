# 📝 To-Do List API

A simple yet production-grade **To-Do List REST API**, built to practice **Software Engineering principles** such as *Clean Code*, *Testing*, *CI/CD*, and *Containerization*.  
The project evolves step-by-step following concepts from **Clean Code** and **The Pragmatic Programmer**.

---

## 🚀 Overview

This API allows users to manage tasks through REST endpoints — create, list, update, and delete to-dos.  
Although simple in purpose, the project is designed as if it were a real product, with attention to:
- modular architecture (routers, services, repositories),
- automated testing and CI/CD,
- Docker and cloud deployment,
- and progressive refactoring.

---

## 🧩 Tech Stack

| Category | Technology |
|-----------|-------------|
| Language | **Python 3.12+** |
| Framework | **FastAPI** |
| Database | **SQLite** → **PostgreSQL** (via Docker Compose) |
| ORM / Models | **SQLAlchemy** or **SQLModel** |
| Testing | **pytest** |
| Containerization | **Docker** |
| CI/CD | **GitHub Actions** |
| Deployment | Local (Docker Compose) → Cloud (Render / GCP Cloud Run) |

---

## 📚 Learning Goals

This project is part of a personal learning path in **Software Engineering**, aiming to:
- Apply *Clean Code* and *Pragmatic Programmer* principles
- Practice automated testing and continuous integration
- Learn Dockerization and CI pipelines
- Understand deployment both locally and in the cloud
- Build maintainable, testable, and readable code

---

## 🗓️ Project Roadmap

| Phase | Description | Status |
|-------|--------------|--------|
| 1 | Repository setup + documentation | ✅ Done |
| 2 | API base (`/health`) | 🚧 In progress |
| 3 | CRUD operations (in-memory → DB) | ⏳ Planned |
| 4 | SQLite / SQLAlchemy integration | ⏳ Planned |
| 5 | Testing & refactoring | ⏳ Planned |
| 6 | Docker & GitHub Actions | ⏳ Planned |
| 7 | Postgres & improvements | ⏳ Planned |
| 8 | Deployment (local + PaaS) | ⏳ Planned |
| 9 | Cloud deployment (GCP Cloud Run) | ⏳ Planned |

---

## 🏗️ Project Structure (planned)

```text
app/
 ├── main.py            # FastAPI entry point
 ├── models/            # Pydantic/SQLModel models
 ├── routers/           # API endpoints
 ├── services/          # Business logic
 ├── repositories/      # DB access layer

tests/
 ├── unit/
 └── integration/
```

*(Will be created progressively as the project evolves.)*

---

## ⚙️ Setup (coming soon)

Instructions for running the app locally and via Docker will appear here once the first endpoints are implemented.

---
