

from fastapi import APIRouter
from schemas import TaskOut, TaskStatus
from app.services.tasks_service import tasks_list_by_employee_and_status


router = APIRouter(
    prefix="/tasks",
    tags=['tasks'],
)

@router.get("", response_model=list[TaskOut])
def get_tasks(employee_id: int, status: TaskStatus):
    return tasks_list_by_employee_and_status(employee_id, status.value)