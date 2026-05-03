from app.core.db import get_connection
import psycopg


def list_employees():
    conn = get_connection()
    try:
        cur = conn.cursor()
        cur.execute('''
            SELECT employee_id, full_name, email, created_at
            FROM employees
            ORDER BY employee_id;
        ''')
        rows = cur.fetchall()
        return rows
    finally:
        conn.close()


def get_employee_by_id(employee_id: int):
    conn = get_connection()
    try:
        cur = conn.cursor()
        cur.execute('''
            SELECT employee_id, full_name, email, created_at
            FROM employees
            WHERE employee_id = %s;
        ''', (employee_id,))
        row = cur.fetchone()
        return row
    finally:
        conn.close()


def create_employee(full_name: str, email: str):
    conn = get_connection()
    try:
        cur = conn.cursor()
        cur.execute('''
            INSERT INTO employees (full_name, email)
            VALUES (%s, %s)
            RETURNING employee_id, full_name, email, created_at;
        ''', (full_name, email))
        new_employee = cur.fetchone()
        conn.commit()
        return new_employee
    except psycopg.IntegrityError:
        conn.rollback()
        return None
    finally:
        conn.close()











