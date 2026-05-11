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


def create_task(description: str, status: str = "pending", employee_id: int = None):
    conn = get_connection()
    try:
        cur = conn.cursor()
        cur.execute(
            """
            INSERT INTO tasks (description, status, employee_id)
            VALUES (%s, %s, %s)
            RETURNING
            task_id,
            description,
            status,
            priority,
            score,
            employee_id,
            created_at;
            """,
            (description, status, employee_id),
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
            ''',
            (employee_id, status)
        )
        rows = cur.fetchall()
        return rows
    finally:
        conn.close()


def get_task_by_id(task_id: int):
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
            WHERE task_id = %s;
            ''',
            (task_id,)
        )
        row = cur.fetchone()
        return row
    finally:
        conn.close()


def update_task_status(task_id: int, new_status: str):
    conn = get_connection()
    try:
        cur = conn.cursor()
        cur.execute(
            '''
            UPDATE tasks
            SET status = %s
            WHERE task_id = %s
            RETURNING
                task_id,
                description,
                status,
                priority,
                score,
                employee_id,
                created_at;
            ''',
            (new_status, task_id)
        )
        update_task = cur.fetchone()
        conn.commit()
        return update_task
    finally:
        conn.close()




















