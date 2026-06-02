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


def update_task_description(task_id: int, new_description: str):
    conn = get_connection()
    try:
        cur = conn.cursor()
        cur.execute(
            '''
            UPDATE tasks
            SET description = %s
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
            (new_description, task_id)
        )
        update_task = cur.fetchone()
        conn.commit()
        return update_task
    finally:
        conn.close()




def get_tasks_stats():
    conn = get_connection()
    try:
        cur = conn.cursor()

        cur.execute(
            '''
            SELECT COUNT(*) AS total_tasks
            FROM tasks;
            '''
        )
        total_row = cur.fetchone()

        cur.execute(
            '''
            SELECT
                COUNT(*) FILTER (WHERE status = 'pending') AS pending,
                COUNT(*) FILTER (WHERE status = 'in_progress') AS in_progress,
                COUNT(*) FILTER (WHERE status = 'completed') AS completed,
                COUNT(*) FILTER (WHERE status = 'blocked') AS blocked
            FROM tasks;
            '''
        )
        status_row = cur.fetchone()

        cur.execute(
            '''
            SELECT
                COUNT(*) FILTER (WHERE priority = 'low') AS low,
                COUNT(*) FILTER (WHERE priority = 'medium') AS medium,
                COUNT(*) FILTER (WHERE priority = 'high') AS high
            FROM tasks;
            '''
        )
        priority_row = cur.fetchone()

        cur.execute(
            '''
            SELECT
                e.employee_id,
                e.full_name,
                COUNT(t.task_id) AS total_tasks,
                COUNT(*) FILTER (WHERE t.status = 'pending') AS pending,
                COUNT(*) FILTER (WHERE t.status = 'in_progress') AS in_progress,
                COUNT(*) FILTER (WHERE t.status = 'completed') AS completed,
                COUNT(*) FILTER (WHERE t.status = 'blocked') AS blocked
            FROM employees e
            LEFT JOIN tasks t
                ON e.employee_id = t.employee_id
            GROUP BY e.employee_id, e.full_name
            ORDER BY total_tasks DESC, e.employee_id ASC;
            '''
        )
        workload_rows = cur.fetchall()

        return {
            "total_tasks": total_row,
            "by_status": status_row,
            "by_priority": priority_row,
            "workload_by_employee": workload_rows,
        }
    finally:
        conn.close()





def update_task_analysis(task_id: int, score: float, priority: str):
    conn = get_connection()
    try:
        cur = conn.cursor()
        cur.execute(
            '''
            UPDATE tasks
            SET
                score = %s,
                priority = %s
            WHERE task_id = %s
            RETURNING
                task_id,
                score,
                priority;
            ''',
            (score, priority, task_id)
        )
        update_task = cur.fetchone()
        conn.commit()
        return update_task
    finally:
        conn.close()






