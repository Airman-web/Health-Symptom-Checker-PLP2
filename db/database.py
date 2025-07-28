# db/database.py
import sqlite3
from pathlib import Path

# Always point to the db file inside the db/ folder, no matter where you run from
DB_PATH = (Path(__file__).resolve().parent / "health.db")

def get_connection():
    """Open a connection to the SQLite database file."""
    return sqlite3.connect(DB_PATH)

def initialize_database():
    """Create tables by executing schema.sql once."""
    conn = get_connection()
    schema_file = Path(__file__).resolve().parent / "schema.sql"
    with open(schema_file, "r") as f:
        conn.executescript(f.read())
    conn.commit()
    conn.close()
