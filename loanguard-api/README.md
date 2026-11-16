# LoanGuard API

Loan Application and Fraud Risk Assessment Backend built with FastAPI.

## Project Description

**LoanGuard API** is a modular REST API designed to process incoming loan applications and perform automated fraud risk assessment. It establishes an architecture that separates API routing, schema validation, persistence models, and risk evaluation engines.

---

## Planned Features

- **Loan Application Submission & Tracking**: Ingest and store structured loan applications with applicant demographics, financials, and loan terms.
- **Automated Fraud Risk Engine**: Evaluate applications against fraud indicators, anomaly checks, and risk scoring matrices.
- **Decision Pipeline**: Classify loans into risk tiers (Low, Medium, High Risk) with actionable recommendation flags.
- **Database Persistence**: Flexible ORM integration (e.g., SQLite for development, PostgreSQL for production).
- **Interactive Documentation**: Auto-generated OpenAPI / Swagger UI at `/docs` and ReDoc at `/redoc`.

---

## Project Structure

```text
loanguard-api/
│
├── app/
│   ├── __init__.py
│   ├── main.py                     # FastAPI application factory and entry point
│   │
│   ├── api/
│   │   ├── __init__.py
│   │   └── routes/
│   │       ├── __init__.py
│   │       └── applications.py     # Loan application router and endpoints
│   │
│   ├── schemas/
│   │   ├── __init__.py
│   │   └── application.py          # Pydantic request/response schemas
│   │
│   ├── services/
│   │   ├── __init__.py
│   │   └── fraud_engine.py         # Fraud assessment and risk evaluation logic
│   │
│   ├── models/
│   │   ├── __init__.py
│   │   └── application.py          # Database ORM models
│   │
│   ├── db/
│   │   ├── __init__.py
│   │   └── session.py              # Database connection and session setup
│   │
│   └── core/
│       ├── __init__.py
│       └── config.py               # Application settings and environment variables
│
├── tests/
│   ├── __init__.py
│   └── test_applications.py       # Unit and integration test suite
│
├── .env.example                    # Template for environment variables
├── .gitignore                      # Git ignore rules for Python, VS Code, and env files
├── requirements.txt                # Core project dependencies
└── README.md                       # Project documentation
```

---

## Installation Instructions

### 1. Clone & Navigate to Project Directory

```bash
cd loanguard-api
```

### 2. Set Up a Virtual Environment

```bash
# Windows
python -m venv venv
.\venv\Scripts\activate

# macOS / Linux
python3 -m venv venv
source venv/bin/activate
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

### 4. Configure Environment Variables

```bash
# Windows (PowerShell)
Copy-Item .env.example .env

# macOS / Linux
cp .env.example .env
```

---

## Running the Application

Start the development server using Uvicorn:

```bash
uvicorn app.main:app --reload --host 127.0.0.1 --port 8000
```

Once running, access:
- **Root Health Check**: [http://127.0.0.1:8000/](http://127.0.0.1:8000/)
- **Interactive API Docs (Swagger UI)**: [http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs)
- **Alternative API Docs (ReDoc)**: [http://127.0.0.1:8000/redoc](http://127.0.0.1:8000/redoc)

---

## Running Tests

Execute test suite using `pytest`:

```bash
pytest
```

