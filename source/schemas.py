

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

class TaskOut(BaseModel):
    task_id: int
    description: str
    status: TaskStatus 
    priority: str | None = None
    score: float | None = None
    employee_id: int | None = None
    created_at: datetime










