

from fastapi import FastAPI
from app.core.logging_config import setup_logging
from app.routers.employees_router import router as employees_router
from app.routers.tasks_router import router as tasks_router
from app.routers.health_router import router as health_router

setup_logging()

app = FastAPI(title="Company API", version="1.0.0")
app.include_router(employees_router)
app.include_router(tasks_router)
app.include_router(health_router)


