

from fastapi import APIRouter, HTTPException, status
from schemas import TaskStatus, TaskCreate, TaskOut, TaskStatusUpdate
from app.services.tasks_service import (
    tasks_list_by_employee_and_status,
    task_get_by_id,
    task_create,
    task_update_status,
)


router = APIRouter(
    prefix="/tasks",
    tags=['tasks'],
)


@router.get("", response_model=list[TaskOut])
def get_tasks(employee_id: int, status: TaskStatus):
    return tasks_list_by_employee_and_status(employee_id, status.value)


@router.get("/{task_id}", response_model=TaskOut)
def get_task_id(task_id: int):
    task = task_get_by_id(task_id)
    
    if task is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail='task not found',
        )
    return task


@router.post("", response_model=TaskOut, status_code=status.HTTP_201_CREATED)
def create_new_task(task_data: TaskCreate):
    new_task = task_create(
        description=task_data.description,
        status=task_data.status,
        employee_id=task_data.employee_id,
    )
    return new_task


@router.patch("/{task_id}/status", response_model=TaskOut)
def update_task_status_route(task_id: int, task_data: TaskStatusUpdate):
    update_task = task_update_status(task_id, task_data.status.value)
    
    if update_task is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail='task not found',
        )
    return update_task

