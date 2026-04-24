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