
import sqlite3
from db_connection import get_connection


# ----------- DAY 1: infraestructura -----------

def test_connection():
    connection = get_connection()
    cursor = connection.cursor()

    cursor.execute('SELECT sqlite_version() AS version;')
    row = cursor.fetchone()

    connection.close()
    print('SQLite version:', row['version'])


def create_employees_table():
    connection = get_connection()
    cursor = connection.cursor()

    cursor.execute('''
        CREATE TABLE IF NOT EXISTS employees (
            employee_id INTEGER PRIMARY KEY,
            full_name TEXT NOT NULL,
            email TEXT NOT NULL UNIQUE,
            created_at TEXT NOT NULL DEFAULT CURRENT_TIMESTAMP
        );
    ''')

    connection.commit()
    connection.close()


def create_employee(full_name: str, email: str) -> bool:
    connection = get_connection()
    cursor = connection.cursor()

    try:
        cursor.execute('''
            INSERT INTO employees (full_name, email)
            VALUES (?, ?);
        ''', (full_name, email))
        connection.commit()
        return True
        
    except sqlite3.IntegrityError:
        connection.rollback()
        return False

    finally:
        connection.close()




def list_employees():
    connection = get_connection()
    try:
        cursor = connection.cursor()
        cursor.execute('''
            SELECT employee_id, full_name, email, created_at
            FROM employees
            ORDER BY employee_id;
        ''')
        rows = cursor.fetchall()
        return rows
    finally:
        connection.close()
    


# ----------- DAY 2: lectura con criterio -----------



def get_employee_by_id(employee_id: int):
    connection = get_connection()
    try:
        cursor = connection.cursor()
        cursor.execute('''
            SELECT employee_id, full_name, email, created_at
            FROM employees
            WHERE employee_id = ?;
        ''', (employee_id,))
        row = cursor.fetchone()
        return row
    finally:
        connection.close()


def print_employee(employee_id: int):
    employee = get_employee_by_id(employee_id)

    if not employee:
        print(f'employee {employee_id} not found')
        return

    print(
        employee['employee_id'],
        employee['full_name'],
        employee['email'],
        employee['created_at']
    )


# ----------- DAY 3: update -----------

def update_employee_email(employee_id: int, new_email: str):
    connection = get_connection()
    cursor = connection.cursor()

    cursor.execute('''
        UPDATE employees
        SET email = ?
        WHERE employee_id = ?;
    ''', (new_email, employee_id))

    if cursor.rowcount == 0:
        print(f'employee {employee_id} not found')
    else:
        print(f'employee {employee_id} updated')

    connection.commit()
    connection.close()


# ----------- DAY 4: delete -----------

def delete_employee(employee_id: int):
    connection = get_connection()
    cursor = connection.cursor()
    
    cursor.execute('''
        DELETE FROM employees
        WHERE employee_id = ?;
    ''', (employee_id,))
    
    if cursor.rowcount == 0:
        print(f'employee {employee_id} not found')
    else:
        print(f'employee {employee_id} deleted')
    
    connection.commit()
    connection.close()

# ----------- DAY 5: join -----------

def create_tasks_table():
    connection = get_connection()
    cursor = connection.cursor()
    
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS tasks(
            task_id INTEGER PRIMARY KEY,
            employee_id INTEGER NOT NULL,
            description TEXT NOT NULL,
            status TEXT NOT NULL DEFAULT 'pending',
            created_at TEXT NOT NULL DEFAULT CURRENT_TIMESTAMP,
            FOREIGN KEY (employee_id) REFERENCES employees(employee_id)
        );
    ''')
    
    connection.commit()
    connection.close()


def create_task(employee_id: int, description: str):
    connection = get_connection()
    cursor = connection.cursor()
    
    cursor.execute('''
        INSERT INTO tasks (employee_id, description)
        VALUES (?, ?);
    ''', (employee_id, description))
    
    connection.commit()
    connection.close()



def list_tasks():
    connection = get_connection()
    cursor = connection.cursor()
    
    cursor.execute('''
        SELECT task_id, employee_id, description, status, created_at
        FROM tasks
        ORDER BY task_id;
    ''')
    
    rows = cursor.fetchall()
    connection.close()
    return rows


def remove_duplicate_tasks():
    connection = get_connection()
    cursor = connection.cursor()
    
    cursor.execute('''
        DELETE FROM tasks
        WHERE task_id NOT IN (
            SELECT MIN(task_id)
            FROM tasks
            GROUP BY employee_id, description
        );
    ''')
    
    connection.commit()
    connection.close()
    print('duplicated tasks removed')


def list_tasks_with_employee():
    connection = get_connection()
    cursor = connection.cursor()
    
    cursor.execute('''
        SELECT
            t.task_id,
            t.description,
            t.status,
            e.full_name,
            e.email
        FROM tasks t
        JOIN employees e
            ON t.employee_id = e.employee_id
        ORDER BY t.task_id;
    ''')
    
    rows = cursor.fetchall()
    connection.close()
    return rows

# ----------- DAY 6:  -----------

def list_tasks_by_status(status: str):
    connection = get_connection()
    cursor = connection.cursor()
    
    cursor.execute('''
        SELECT task_id, description, status
        FROM tasks
        WHERE status = ?;
    ''', (status,))
    
    rows = cursor.fetchall()
    connection.close()
    return rows



def list_tasks_by_employee(employee_id: int):
    connection = get_connection()
    cursor = connection.cursor()
    
    cursor.execute('''
        SELECT task_id, description, status
        FROM tasks
        WHERE employee_id = ?;
    ''', (employee_id,))
    
    rows = cursor.fetchall()
    connection.close()
    return rows



def list_tasks_by_employee_and_status(employee_id: int, status: str):
    connection = get_connection()
    cursor = connection.cursor()
    
    cursor.execute('''
        SELECT task_id, description, status
        FROM tasks
        WHERE employee_id = ?
        AND status = ?;
    ''', (employee_id, status))
    
    rows = cursor.fetchall()
    connection.close()
    return rows






