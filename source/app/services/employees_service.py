
import logging
from main import list_employees, get_employee_by_id, create_employee


logger = logging.getLogger(__name__)



def employees_list():
    logger.info('employees_list called')
    rows = list_employees()
    return [dict(r) for r in rows]

def employee_get(employee_id: int):
    logger.info('employee_get called | employee_id:%s', employee_id)
    row = get_employee_by_id(employee_id)
    return dict(row) if row else None

def employee_create(full_name: str, email: str):
    logger.info('employee_create called | email:%s', email)
    return create_employee(full_name, email)



