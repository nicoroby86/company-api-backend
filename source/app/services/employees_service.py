import logging
from app.dal.employees_dal import (
    list_employees,
    get_employee_by_id,
    create_employee,
)


logger = logging.getLogger(__name__)


def employees_list():
    logger.info('employees_list called')
    rows = list_employees()
    return rows


def employee_get(employee_id: int):
    logger.info('employee_get called | employee_id:%s', employee_id)
    row = get_employee_by_id(employee_id)
    return row


def employee_create(full_name: str, email: str):
    logger.info('employee_create called | email:%s', email)
    row = create_employee(full_name, email)
    return row




