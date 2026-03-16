

from schemas import EmployeeCreate
from main import create_employee
from fastapi import HTTPException
from fastapi import FastAPI
from main import (
    list_employees,
    get_employee_by_id,
    list_tasks_by_employee_and_status,
)

app = FastAPI()


# endpoint 1 (empleados) -> list_employees

@app.get("/employees")
def get_all_employees():
    return list_employees()



# endpoint 2 (empleado por ID) -> get_employee_by_id

@app.get("/employees/{employee_id}")
def get_employee(employee_id: int):
    return get_employee_by_id(employee_id)


# endpoint 3 (tareas por empleado y estado) -> list_tasks_by_employee_and_status

@app.get("/tasks")
def get_tasks(employee_id: int, status: str):
    return list_tasks_by_employee_and_status(employee_id, status)



@app.post("/employees", status_code=201)
def create_new_employee(employee: EmployeeCreate):
    ok = create_employee(employee.full_name, employee.email)
    
    if not ok:
        raise HTTPException(status_code=400, detail='email already exists')
    
    return {'message:' 'employee created'}








