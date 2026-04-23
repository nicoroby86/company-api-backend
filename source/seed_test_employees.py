

from db_connection import get_connection
import sqlite3

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

def seed_employees() -> None:
    print('\n[SEED EMPLOYEES START]')
    employees = [
        ("Ana Lopez", "ana@empresa.com"),
        ("Bruno Diaz", "bruno@empresa.com"),
        ("Carla Ruiz", "carla@empresa.com"),
    ]
    for full_name, email in employees:
        created = create_employee(full_name, email)
        if created:
            print(f'Employee created: {full_name} | {email}')
        else:
            print(f'Could not create employee: {full_name} | {email}')
    
    print('[SEED EMPLOYEES END]\n')

if __name__ == "__main__":
    seed_employees()
























