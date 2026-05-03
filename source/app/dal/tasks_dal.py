from app.core.db import get_connection


def list_tasks():
    conn = get_connection()
    try:
        cur = conn.cursor()
        cur.execute("""
            SELECT task_id, description, status
            FROM tasks
            ORDER BY task_id;
        """)
        rows = cur.fetchall()
        return rows
    finally:
        conn.close()


def create_task(description: str, status: str = "pending"):
    conn = get_connection()
    try:
        cur = conn.cursor()
        cur.execute(
            """
            INSERT INTO tasks (description, status)
            VALUES (%s, %s)
            RETURNING task_id, description, status;
            """,
            (description, status),
        )
        new_task = cur.fetchone()
        conn.commit()
        return new_task
    finally:
        conn.close()


def list_tasks_by_employee_and_status(employee_id: int, status: str):
    conn = get_connection()
    try:
        cur = conn.cursor()
        cur.execute(
            '''
            SELECT
                task_id,
                description,
                status,
                priority,
                score,
                employee_id,
                created_at
            FROM tasks
            WHERE employee_id = %s
                AND status = %s
            ORDER BY task_id;
            ''', (employee_id, status)
        )
        rows = cur.fetchall()
        return rows
    finally:
        conn.close()