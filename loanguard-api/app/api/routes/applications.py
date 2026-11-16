"""Loan application API routes."""

from fastapi import APIRouter

router = APIRouter(
    prefix="/applications",
    tags=["applications"],
)

# TODO: Define loan application endpoints (e.g., submit application, get status, list applications)