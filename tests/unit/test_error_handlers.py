import pytest
from fastapi import FastAPI, HTTPException
from fastapi.testclient import TestClient

from app.core.error_handlers import setup_exception_handlers


@pytest.fixture
def app():
    app = FastAPI()
    setup_exception_handlers(app)

    @app.get("/http-error")
    def http_error():
        raise HTTPException(status_code=400, detail="Bad request")

    @app.get("/validation-error")
    def validation_error(item: int):
        return {"item": item}

    @app.get("/generic-error")
    def generic_error():
        raise Exception("Unexpected error")

    return app


@pytest.fixture
def client(app):
    return TestClient(app, raise_server_exceptions=False)


def test_http_exception_handler(client):
    resp = client.get("/http-error")
    assert resp.status_code == 400
    assert resp.json()["error"] == 400
    assert resp.json()["message"] == "Bad request"


def test_validation_exception_handler(client):
    resp = client.get("/validation-error?item=not-an-int")
    assert resp.status_code == 422
    assert resp.json()["error"] == "Validation Error"


def test_generic_exception_handler(client):
    resp = client.get("/generic-error")
    assert resp.status_code == 500
    assert resp.json()["error"] == "Internal Server Error"
