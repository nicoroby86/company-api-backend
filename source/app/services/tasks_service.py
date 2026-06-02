

import logging
from typing import Any

from app.dal.tasks_dal import (
    list_tasks_by_employee_and_status,
    get_task_by_id,
    create_task,
    update_task_status,
    update_task_description,
    get_tasks_stats,
    update_task_analysis,
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


def task_update_description(task_id: int, new_description: str):
    logger.info(
        'task_update_description called | task_id:%s | new_description:%s',
        task_id,
        new_description,
    )
    
    update_task = update_task_description(task_id, new_description)
    return update_task


def tasks_get_stats():
    logger.info('tasks_get_stats called')

    stats = get_tasks_stats()

    total_tasks = stats["total_tasks"]["total_tasks"]

    by_status = {
        "pending": stats["by_status"]["pending"],
        "in_progress": stats["by_status"]["in_progress"],
        "completed": stats["by_status"]["completed"],
        "blocked": stats["by_status"]["blocked"],
    }

    by_priority = {
        "low": stats["by_priority"]["low"],
        "medium": stats["by_priority"]["medium"],
        "high": stats["by_priority"]["high"],
    }

    workload_by_employee = []

    for row in stats["workload_by_employee"]:
        workload_by_employee.append(
            {
                "employee_id": row["employee_id"],
                "full_name": row["full_name"],
                "total_tasks": row["total_tasks"],
                "pending": row["pending"],
                "in_progress": row["in_progress"],
                "completed": row["completed"],
                "blocked": row["blocked"],
            }
        )

    return {
        "total_tasks": total_tasks,
        "by_status": by_status,
        "by_priority": by_priority,
        "workload_by_employee": workload_by_employee,
    }




def analyze_task_description(description: str, current_status: str):
    description_lower = description.lower()
    
    score = 0.0
    reasons = []
    
    high_priority_keywords = {
        "urgent": 0.25,
        "asap": 0.25,
        "critical": 0.25,
        "production": 0.20,
        "bug": 0.20,
        "error": 0.20,
        "failed": 0.20,
        "failure": 0.20,
        "broken": 0.20,
        "blocked": 0.20,
        "fix": 0.10,
    }
    
    medium_priority_keywords = {
        "database": 0.15,
        "postgresql": 0.15,
        "connection": 0.15,
        "deployment": 0.15,
        "deploy": 0.15,
        "api": 0.10,
        "endpoint": 0.10,
        "testing": 0.10,
        "test": 0.10,
        "validation": 0.10,
        "review": 0.05,
    }
    
    for keyword, weight in high_priority_keywords.items():
        if keyword in description_lower:
            score += weight
            reasons.append(f'contains high-priority keyword: {keyword}')
    
    for keyword, weight in medium_priority_keywords.items():
        if keyword in description_lower:
            score += weight
            reasons.append(f'contains technical keyword: {keyword}')
    
    if current_status == 'blocked':
        score += 0.20
        reasons.append('task is currently blocked')
    
    elif current_status == 'in_progress':
        score += 0.05
        reasons.append('task is currently in progress')
    
    if len(description) >= 80:
        score += 0.10
        reasons.append('long description with additional context')
    
    if len(description) < 25:
        reasons.append('short description with limited context')
    
    if score > 1.0:
        score = 1.0
    
    score = round(score, 2)
    
    if score >= 0.65:
        priority = 'high'
    elif score >= 0.30:
        priority = 'medium'
    else:
        priority = 'low'
    
    if not reasons:
        reasons.append('no relevant priority indicators detected')
    
    return score, priority, reasons



def task_analyze(task_id: int):
    logger.info(
        'task_analyze called | task_id:%s',
        task_id,
    )
    
    task = get_task_by_id(task_id)
    
    if task is None:
        return None
    
    description = task["description"]
    current_status = task["status"]
    
    score, priority, reasons = analyze_task_description(
        description=description,
        current_status=current_status,
    )
    
    update_task_analysis(
        task_id=task_id,
        score=score,
        priority=priority,
    )
    
    return {
        "task_id": task_id,
        "description": description,
        "score": score,
        "priority": priority,
        "reasons": reasons,
    }






