"""
init_db.py

Initializes the SQLite database and inserts demo employee data.

Run from project root:
    python init_db.py
"""

from __future__ import annotations

import sys
from pathlib import Path


PROJECT_ROOT = Path(__file__).resolve().parent
SOURCE_DIR = PROJECT_ROOT / "source"
DATABASE_DIR = PROJECT_ROOT / "database"

# Allow importing from /source (where your main.py lives)
sys.path.insert(0, str(SOURCE_DIR))


def main() -> None:
    # Ensure database/ folder exists
    DATABASE_DIR.mkdir(parents=True, exist_ok=True)

    # Import your existing functions from source/main.py
    from main import create_employees_table, create_employee  # type: ignore

    # Create tables
    create_employees_table()

    # Insert demo data (won't crash if already exists)
    created = create_employee("Demo User", "demo@example.com")
    if created:
        print("[init_db] Database initialized with demo employee ✅")
    else:
        print("[init_db] Database already initialized (demo user exists) ✅")


if __name__ == "__main__":
    main()