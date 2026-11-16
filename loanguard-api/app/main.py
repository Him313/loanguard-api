"""FastAPI application entry point for LoanGuard API."""

from fastapi import FastAPI

from app.api.routes.applications import router as applications_router
from app.core.config import settings

app = FastAPI(
    title=settings.PROJECT_NAME,
    openapi_url=f"{settings.API_V1_STR}/openapi.json",
)

# Include application routes
app.include_router(applications_router, prefix=settings.API_V1_STR)


@app.get("/", tags=["health"])
def health_check():
    """Basic root health check endpoint."""
    return {
        "project": settings.PROJECT_NAME,
        "status": "healthy",
        "environment": settings.ENVIRONMENT,
    }

