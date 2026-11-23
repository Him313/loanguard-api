"""Loan application API routes."""
from fastapi import APIRouter, HTTPException
from app.schemas.application import ApplicationBase

router = APIRouter(
    prefix="/loan-guard",
    tags=["applications"],
)

## create a new loan application
@router.post('/applications')
def submit_application(application: ApplicationBase):
    return {"message": "Application submitted successfully", "data": application}

## Retreive a single application
@router.get('/applications/{application_id}')
def get_status(application_id: int):
    return {"message": f"Application status for {application_id}"}

## retreive all applications
@router.get('/applications')
def list_applications():
    return {"message": "List of applications"}

## update a single application
@router.put('/applications/{application_id}')
def update_application(application_id: int):
    return {"message": f"Application updated successfully for {application_id}"}

## delete a single application
@router.delete('/applications/{application_id}')
def delete_application(application_id: int):
    return {"message": f"Application deleted successfully for {application_id}"}

## update application review status
@router.put('/applications/{application_id}/status')
def update_review_status(application_id: int):
    return {"message": f"Application review status for {application_id}"}

## retreive high risk cuastomers
@router.get('/applications/high-risk')
def get_high_risk_customers():
    return {"message": "List of high-risk customers"}

## retreive all high risk customers
@router.get('/applications/high-risk/all')
def get_all_high_risk_customers():
    return {"message": "List of all high-risk customers"}

## get dashboard metrics
@router.get('/applications/dashboard')
def get_dashboard_metrics():
    return {"message": "List of dashboard metrics"}