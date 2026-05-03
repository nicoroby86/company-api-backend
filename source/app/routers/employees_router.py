from fastapi import APIRouter, HTTPException, status
from schemas import EmployeeCreate, EmployeeOut
from app.services.employees_service import employees_list, employee_get, employee_create


router = APIRouter(
    prefix="/employees",
    tags=['employees'],
)


@router.get("", response_model=list[EmployeeOut])
def get_all_employees():
    return employees_list()


@router.get("/{employee_id}", response_model=EmployeeOut)
def get_employee(employee_id: int):
    employee = employee_get(employee_id)
    if employee is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail='employee not found',
        )
    return employee


@router.post("", response_model=EmployeeOut, status_code=status.HTTP_201_CREATED)
def create_new_employee(employee: EmployeeCreate):
    new_employee = employee_create(employee.full_name, employee.email)
    if new_employee is None:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail='email already exists',
        )
    return new_employee