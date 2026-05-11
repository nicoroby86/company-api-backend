
# Company API — PostgreSQL Refactor

A backend REST API built with **FastAPI + PostgreSQL**, following a layered architecture with **routers / services / DAL / core**, typed contracts using **Pydantic**, and environment-based configuration.

This repository started as a **V1 built with SQLite** and is currently evolving into a more deployable **V2** using PostgreSQL as the active database layer.

---

## Current Status

The PostgreSQL-based V2 flow currently includes:

## Current Status

The PostgreSQL-based V2 flow currently includes:

- `GET /employees`
- `GET /employees/{employee_id}`
- `POST /employees`
- `GET /tasks?employee_id=...&status=...`
- `GET /tasks/{task_id}`
- `POST /tasks`
- `PATCH /tasks/{task_id}/status`
- `GET /health`

### Current application flow:

```text
router -> service -> DAL -> PostgreSQL
```

## Database

- Active database: PostgreSQL
- Environment-based configuration through .env
- Health check verifies DB connectivity using SELECT 1

---

## Live Demo

The PostgreSQL-based V2 API is publicly deployed on Render.

- Health check: `https://company-api-web.onrender.com/health`
- Swagger Docs: `https://company-api-web.onrender.com/docs`

This deployment includes:
- FastAPI Web Service on Render
- PostgreSQL database on Render
- public API documentation
- remote database connectivity

---

## Tech Stack

### V2 (current)
- FastAPI
- PostgreSQL
- Psycopg
- Pydantic
- Python-dotenv
- Uvicorn

### V1 (baseline)
- FastAPI
- SQLite
- Pydantic
- Uvicorn

---

## Features

### Current V2 features
- **PostgreSQL** connection through environment variables
- **Layered architecture**
  - routers
  - services
  - DAL
  - core
- Employee endpoints migrated to PostgreSQL
- Tasks endpoint migrated to PostgreSQL
- Health check endpoint for DB connectivity
- Typed request/response contracts with Pydantic
- Logging setup for application flow
- Local environment config through `.env`

### V1 foundation preserved in the project history
- **FastAPI + SQLite baseline**
- Initial layered structure
- Manual and automated testing
- Postman collection
- Validation with Pydantic
- Logging and structured error handling

---

## Example Responses

GET /employees
[
  {
    "employee_id": 1,
    "full_name": "Ana Torres",
    "email": "ana@example.com",
    "created_at": "2026-05-01T17:43:13.571536"
  }
]

POST /employees
{
  "employee_id": 1,
  "full_name": "Ana Torres",
  "email": "ana@example.com",
  "created_at": "2026-05-01T17:43:13.571536"
}

GET /tasks?employee_id=1&status=pending
[
  {
    "task_id": 1,
    "description": "Prepare API deployment",
    "status": "pending",
    "priority": null,
    "score": null,
    "employee_id": 1,
    "created_at": "2026-05-01T18:15:07.524885"
  }
]

GET /health
{
  "status": "ok",
  "database": "connected"
}

---

## Project Structure

```text
company-api-fastapi-v1/
├── README.md
├── requirements.txt
├── .gitignore
├── .env.example
├── testing.md
├── assets/
├── database/                      # runtime/local artifacts (SQLite legacy area)
├── postman/
│   └── company-api-v1.postman_collection.json
└── source/
    ├── api_legacy.py             # historical monolithic version
    ├── main.py                   # legacy V1 helpers still present during refactor
    ├── schemas.py                # Pydantic schemas
    ├── logs/                     # runtime logs
    ├── scripts/
    │   └── test_connection.py    # PostgreSQL connection check
    ├── tests/
    ├── app/
    │   ├── api.py                # FastAPI entrypoint
    │   ├── core/
    │   │   ├── config.py         # environment-based settings
    │   │   ├── db.py             # PostgreSQL connection
    │   │   └── logging_config.py
    │   ├── dal/
    │   │   ├── employees_dal.py
    │   │   └── tasks_dal.py
    │   ├── routers/
    │   │   ├── employees_router.py
    │   │   ├── tasks_router.py
    │   │   └── health_router.py
    │   └── services/
    │       ├── employees_service.py
    │       └── tasks_service.py
```

---

## Requirements

- Python 3.10+ recommended
- PostgreSQL running locally

---

## Local Setup (V2)

1) Create and activate a virtual environment

**Windows (PowerShell):**

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
```

**macOS / Linux:**

```bash
python3 -m venv .venv
source .venv/bin/activate
```

2) Install dependencies

```bash
pip install -r requirements.txt
```

3) Create `.env`

Use `.env.example` as reference:

```env
DB_HOST=localhost
DB_PORT=5432
DB_NAME=company_db
DB_USER=your_postgres_user
DB_PASSWORD=your_postgres_password

4) Create PostgreSQL tables

At this stage of the refactor, tables are created directly in PostgreSQL during local setup.

5) Run the API

```bash
cd source
uvicorn app.api:app --reload
```

Open Swagger UI:

http://127.0.0.1:8000/docs

---

## Status Codes

- `200 OK` — Successful request
- `201 Created` — Resource created successfully
- `400 Bad Request` — Business rule violation (e.g. duplicate email)
- `404 Not Found` — Resource not found
- `422 Unprocessable Entity` — Validation error
- `503 Service Unavailable` — Database unavailable (/health)

## Logging

This API uses Python's built-in `logging` module to track requests and service-layer actions.

Logs are printed to the console and also written to runtime log files:

- `logs/app.log`

**Typical log line**

```text
2026-05-01 13:16:17,674 | INFO | app.services.employees_service | employee_create called | email: ana@example.com
```

---

## Project Evolution

### V1 — SQLite baseline

V1 was the original version of the project and served as the foundation for the current refactor.

It focused on:

- FastAPI fundamentals
- SQLite integration
- routers / services / core structure
- Pydantic validation
- manual and automated testing
- logging
- API documentation
- Postman collection support

In V1:

- the active database was SQLite
- created_at was handled as a string
- POST /employees returned a simple confirmation message
- the architecture was simpler, but intentionally designed to make the V2 refactor possible

### V2 — PostgreSQL refactor

V2 is the active direction of the project.

It introduces:

- PostgreSQL as the active database
- DAL-based access layer
- environment-based configuration
- /health endpoint for DB readiness
- response contracts aligned with PostgreSQL types
- better preparation for deployment

This version reflects a more realistic backend workflow and is the base for the upcoming public deploy.

---

## How to test quickly

You can validate the API quickly using Swagger or curl.

### Swagger (UI)

Run the API and open:

```text
http://127.0.0.1:8000/docs
```

Use Swagger to:
- Explore endpoints
- Send requests interactively
- Inspect request/response structure
- Validate happy paths quickly

### Terminal requests

Useful for testing raw HTTP behavior and debugging.

#### Create an employee

**Windows PowerShell**

```powershell
$body = @{
    full_name = "Esteban Martinez"
    email = "esteban@example.com"
} | ConvertTo-Json

Invoke-RestMethod `
    -Uri "http://127.0.0.1:8000/employees" `
    -Method Post `
    -ContentType "application/json" `
    -Body $body
```

**Linux / macOS / Git Bash**

```bash
curl -X POST "http://127.0.0.1:8000/employees" \
-H "Content-Type: application/json" \
-d '{
  "full_name": "Pedro Alvarez",
  "email": "pedro@example.com"
}'

```


#### Get all employees

**Windows PowerShell**

```powershell
curl.exe -i "http://127.0.0.1:8000/employees"
```

**Linux / macOS / Git Bash**

```bash
curl -i "http://127.0.0.1:8000/employees"
```

#### Get employee by ID

**Windows PowerShell**

```powershell
curl.exe -i "http://127.0.0.1:8000/employees/1"
```

**Linux / macOS / Git Bash**

```bash
curl -i "http://127.0.0.1:8000/employees/1"
```

#### Get tasks by employee and status

**Windows PowerShell**

```powershell
curl.exe -i "http://127.0.0.1:8000/tasks?employee_id=1&status=pending"
```

**Linux / macOS / Git Bash**

```bash
curl -i "http://127.0.0.1:8000/tasks?employee_id=1&status=pending"
```

#### Get health

**Windows PowerShell**

```powershell
curl.exe -i "http://127.0.0.1:8000/health"
```

**Linux / macOS / Git Bash**

```bash
curl -i "http://127.0.0.1:8000/health"
```

#### Expected behavior

- Duplicate email → `400 Bad Request`
- Invalid email format → `422 Unprocessable Entity`
- Non-existing employee → `404 Not Found`
- No tasks found → `200 OK` with `[]`

---

## Testing

This project includes both the original V1 testing foundation and the ongoing validation of the PostgreSQL-based V2 refactor.

### Testing approaches

#### Swagger (Interactive Testing)
- Quick endpoint validation
- Request/response inspection
- Status code and contract checks

#### curl (Terminal Testing)
- Raw HTTP verification
- Header, status code, and JSON response inspection
- Useful for validation and debugging during migration

#### Postman
- Structured manual testing with saved requests
- Reproducible request flows
- Validation of happy paths and error cases

#### Pytest
- Automated endpoint testing
- Contract and validation checks
- Regression support as the project evolves

### Quick test coverage

The project has been validated across these scenarios:

- successful requests (`200`, `201`)
- duplicate email handling (`400`)
- validation errors (`422`)
- missing resources (`404`)
- empty collections (`200` with `[]`)
- filtered task retrieval (`GET /tasks?employee_id=...&status=...`)
- database connectivity (`GET /health`)

### Project testing assets

The repository includes:

- `testing.md`
- `postman/company-api-v1.postman_collection.json`
- automated tests in `source/tests/`

### Run automated tests

From project root:

```bash
python -m pytest -v
```
- Uses FastAPI `TestClient`
- Runs tests without needing the server running
- Ensures endpoint behavior and contracts remain stable

---

These tests ensure the API behaves consistently across manual and automated validation layers.

---

## What this project demonstrates
- API design with FastAPI
- migration from SQLite to PostgreSQL
- layered backend structure
- DAL-based database access
- response contract evolution
- environment-based configuration
- incremental refactoring inside a Git branch
- realistic backend portfolio progression

---

## Repository Status

### Current direction of the project:

- V1: SQLite baseline
- V2: PostgreSQL migration in progress
- Next: first public deploy on Render

---

## Pre-release Checklist

Before publishing or cloning the project:

1) `database/company.db` is NOT tracked  
2) `logs/app.log` is NOT tracked  
3) `cd source` + `uvicorn app.api:app --reload` works  

You can use `git status` to verify which files are staged before committing.