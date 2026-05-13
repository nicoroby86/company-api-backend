

from enum import Enum
from datetime import datetime
from pydantic import BaseModel, EmailStr


class EmployeeCreate(BaseModel):
    full_name: str
    email: EmailStr


class EmployeeOut(BaseModel):
    employee_id: int
    full_name: str
    email: EmailStr
    created_at: datetime


class TaskStatus(str, Enum):
    pending = 'pending'
    in_progress = 'in_progress'
    completed = 'completed'
    blocked = 'blocked'


class TaskCreate(BaseModel):
    description: str
    status: TaskStatus = TaskStatus.pending
    employee_id: int


class TaskStatusUpdate(BaseModel):
    status: TaskStatus


class TaskDescriptionUpdate(BaseModel):
    description: str


class TaskOut(BaseModel):
    task_id: int
    description: str
    status: TaskStatus 
    priority: str | None = None
    score: float | None = None
    employee_id: int | None = None
    created_at: datetime


class TaskStatusStats(BaseModel):
    pending: int
    in_progress: int
    completed: int
    blocked: int


class TaskPriorityStats(BaseModel):
    low: int
    medium: int
    high: int


class EmployeeWorkloadStats(BaseModel):
    employee_id: int
    full_name: str
    total_tasks: int
    pending: int
    in_progress: int
    completed: int
    blocked: int


class TaskStatsOut(BaseModel):
    total_tasks: int
    by_status: TaskStatusStats
    by_priority: TaskPriorityStats
    workload_by_employee: list[EmployeeWorkloadStats]

