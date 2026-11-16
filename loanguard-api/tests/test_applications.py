"""Tests for LoanGuard API application initialization and routes."""

from app.main import app


def test_app_initialization():
    """Verify that the FastAPI application initializes with correct configuration."""
    assert app.title == "LoanGuard API"
    assert app.openapi_url == "/api/v1/openapi.json"


def test_openapi_schema_generation():
    """Verify that the OpenAPI schema compiles successfully."""
    schema = app.openapi()
    assert schema["info"]["title"] == "LoanGuard API"
    assert "/" in schema["paths"]


# TODO: Add unit and integration tests for loan applications and fraud risk assessment
# Example for endpoint tests once routes are implemented:
# from fastapi.testclient import TestClient
# client = TestClient(app)
# def test_read_root():
#     response = client.get("/")
#     assert response.status_code == 200
