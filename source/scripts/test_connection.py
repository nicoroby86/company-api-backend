from app.core.db import get_connection


def test_connection():
    conn = get_connection()
    try:
        cur = conn.cursor()
        cur.execute("SELECT 1;")

        result = cur.fetchone()
        print('Resultado:', result)
    finally:
        conn.close()


if __name__ == "__main__":
    test_connection()