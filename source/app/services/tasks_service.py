

import logging
from typing import Any

from main import list_tasks_by_employee_and_status

logger = logging.getLogger(__name__)


def tasks_list_by_employee_and_status(employee_id: int, status: str) -> list[dict[str, Any]]:
    logger.info(
        'tasks_list_by_employee_and_status called | employee_id:%s | status:%s',
        employee_id,
        status,
    )
    
    rows = list_tasks_by_employee_and_status(employee_id, status)
    return [dict(r) for r in rows]
