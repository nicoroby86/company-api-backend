

import logging
from typing import Any

from app.dal.tasks_dal import (
    list_tasks_by_employee_and_status,
    get_task_by_id,
    create_task,
    update_task_status,
)


logger = logging.getLogger(__name__)


def tasks_list_by_employee_and_status(employee_id: int, status: str) -> list[dict[str, Any]]:
    logger.info(
        'tasks_list_by_employee_and_status called | employee_id:%s | status:%s',
        employee_id,
        status,
    )
    
    rows = list_tasks_by_employee_and_status(employee_id, status)
    return rows


def task_get_by_id(task_id: int):
    logger.info(
        'task_get_by_id called | task_id:%s',
        task_id,
    )
    
    row = get_task_by_id(task_id)
    return row

def task_create(description: str, status: str = "pending", employee_id: int | None = None):
    logger.info(
        'task_create called | description:%s | status:%s | employee_id:%s',
        description,
        status,
        employee_id,
    )
    
    new_task = create_task(description, status, employee_id)
    return new_task


def task_update_status(task_id: int, new_status: str):
    logger.info(
        'task_update_status called | task_id:%s | new_status:%s',
        task_id,
        new_status,
    )
    
    update_task = update_task_status(task_id, new_status)
    return update_task
