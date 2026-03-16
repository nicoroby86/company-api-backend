
# Company API (V1) — Employees & Tasks

A small but production-style REST API built with **FastAPI + SQLite**, following a clean architecture (**routers / services / core**), typed contracts using **Pydantic**, and consistent logging.

This project is part of my backend portfolio and focuses on correctness, clarity, and real-world structure.

---

## Tech Stack

- FastAPI
- SQLite
- Pydantic
- Uvicorn

---

## Features

- **FastAPI** + interactive docs (Swagger/OpenAPI)
- **SQLite** database with constraints (e.g., unique email)
- **Pydantic models**
  - Request model: `EmployeeCreate`
  - Response models: `EmployeeOut`, `TaskOut`
- **Service layer** that converts SQLite `Row` → JSON-serializable `dict`
- **Logging**
  - Console logs
  - File logs (generated at runtime)
- **Input validation**
  - Email validation via `EmailStr`
  - Task status validation via Enum (`TaskStatus`)

---

## Project Structure

```text
company-api-v1/
├── README.md
├── requirements.txt
├── .gitignore
├── init_db.py
├── database/               # created/used at runtime (DB file is ignored by git)
└── source/
    ├── main.py             # DB functions (learning + utilities)
    ├── db_connection.py    # SQLite connection helper
    ├── schemas.py          # Pydantic schemas
    ├── api_legacy.py       # initial monolithic version (historical)
    ├── logs/               # log file generated at runtime (ignored by git)
    └── app/
        ├── api.py          # FastAPI app entrypoint
        ├── core/
        │   ├── db.py
        │   └── logging_config.py
        ├── routers/
        │   ├── employees_router.py
        │   └── tasks_router.py
        └── services/
            ├── employees_service.py
            └── tasks_service.py
```
> Note: `database/company.db` and `logs/app.log` are generated locally and ignored by git.


## Requirements

- Python **3.10+** (recommended: 3.11+)

---

## Setup (Run Locally)

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

3) Initialize the database (creates tables + inserts demo employee)

```bash
python init_db.py
```

4) Run the API

```bash
cd source
uvicorn app.api:app --reload
```

Open Swagger UI:

http://127.0.0.1:8000/docs


---

## Endpoints

### GET /employees

Returns the list of all employees.

**Response**
```json
[
  {
    "employee_id": 1,
    "full_name": "Pedro Ciruja",
    "email": "pedro@example.com",
    "created_at": "2026-02-03T18:42:11"
  }
]
```

### GET /employees/{employee_id}

Returns a single employee by ID.

**Response**
```json
{
  "employee_id": 1,
  "full_name": "Pedro Ciruja",
  "email": "pedro@example.com",
  "created_at": "2026-02-03T18:42:11"
}
```

### POST /employees

Creates a new employee.

**Request body**
```json
{
  "full_name": "Pedro Ciruja",
  "email": "pedro@example.com"
}
```

**Success response (201 Created)**
```json
{
  "message": "employee created"
}
```

### GET /tasks

Returns tasks for a specific employee, filtered by status.

**Query params**
- `employee_id` (int, required)
- `status` (enum, optional, default: `pending`)

> In V1, only `status="pending"` is supported.

**Response**
```json
[
  {
    "task_id": 1,
    "description": "Update emails",
    "status": "pending"
  }
]
```

---

## Status Codes

- `200 OK` — Successful request (GET endpoints)
- `201 Created` — Employee created successfully (POST /employees)
- `400 Bad Request` — Business rule violation (e.g., duplicate email)
- `404 Not Found` — Employee not found (GET /employees/{employee_id})
- `422 Unprocessable Entity` — Validation error (invalid request body or invalid query params, e.g. wrong email format)



## Logging

This API uses Python's built-in `logging` module to track requests and service-layer actions.

Logs are printed to the console and also written to:

- `logs/app.log`

**Typical log line**

```text
2026-02-04 12:23:59,031 | INFO | app.services.employees_service | employee_create called | email: pedro@example.com
```

## Notes

- SQLite is used as the database for V1.
- Timestamps are stored as text in SQLite (via `CURRENT_TIMESTAMP`), so `created_at` is returned as a string in V1.
- The architecture is intentionally simple but scalable (routers/services/core), and ready for a V2 refactor (PostgreSQL + Alembic + Docker + tests).

---

## How to test quickly


### Swagger (UI)

Run the API and open:

http://127.0.0.1:8000/docs

From there you can test all endpoints interactively.


### Using curl (terminal)


#### Create an employee

```bash
curl -X POST "http://127.0.0.1:8000/employees" \
-H "Content-Type: application/json" \
-d '{
  "full_name": "Pedro Ciruja",
  "email": "pedro@example.com"
}'

```

#### Get all employees

```bash
curl "http://127.0.0.1:8000/employees"
```

#### Get employee by ID

```bash
curl "http://127.0.0.1:8000/employees/1"
```

#### Get tasks by employee and status

```bash
curl "http://127.0.0.1:8000/tasks?employee_id=1&status=pending"
```

#### Expected behavior

Duplicate email → 400 Bad Request

Invalid email format → 422 Unprocessable Entity

Non-existing employee → 404 Not Found

No tasks found → 200 OK with empty list

---

## Future Improvements (V2)

This V1 version was intentionally built using a simple architecture and SQLite to focus on core backend principles, API design, data integrity, and service separation.

The next iteration (V2) will evolve this project into a more production-ready backend by introducing:

- Migration from SQLite → PostgreSQL  
- Database versioning using Alembic  
- Containerization with Docker  
- Automated testing with pytest  
- Environment configuration via `.env`  
- Improved error handling and validation patterns  
- Clear separation between development and production settings  
- Structured logging improvements  
- API documentation refinements  

The current structure (routers / services / core) was designed from the beginning to make this refactor natural and possible without rewriting the business logic.

V2 aims to transform this API from a learning project into a portfolio-grade backend service aligned with real-world backend practices.


## Pre-release Checklist

Before publishing or cloning the project:

1) `database/company.db` is NOT tracked  
2) `logs/app.log` is NOT tracked  
3) From project root: `python init_db.py` works  
4) `cd source` + `uvicorn app.api:app --reload` works  

You can use `git status` to verify which files are staged before committing.