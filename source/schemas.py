

from enum import Enum
from pydantic import BaseModel, EmailStr


class EmployeeCreate(BaseModel):
    full_name: str
    email: EmailStr


class EmployeeOut(BaseModel):
    employee_id: int
    full_name: str
    email: EmailStr
    created_at: str


class TaskOut(BaseModel):
    task_id: int
    description: str
    status: str


class TaskStatus(str, Enum):
    pending = 'pending'







