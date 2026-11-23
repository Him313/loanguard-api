from pydantic import BaseModel, Field

# TODO: Define application schemas (e.g., ApplicationCreate, ApplicationResponse, ApplicationUpdate)
# Example placeholder:
class ApplicationBase(BaseModel):
    applicant_name: str
    age: int = Field(gt=0, le=120)
    annual_income: float = Field(ge=0)
    loan_amount: float = Field(ge=0)
    credit_score: int = Field(ge=300, le=850)
    loan_term_months: int = Field(ge=6, le=60)

