# modules/history.py
import mysql.connector
from mysql.connector import Error
from db.database import get_connection  # Assumes you have this function returning a DB connection

def init_db():
    """
    Initialize the database tables if they don't exist yet.
    Call this once when starting your app.
    """
    conn = get_connection()
    cursor = conn.cursor()
    
    # Drop existing tables first (in correct order due to foreign keys)
    cursor.execute('DROP TABLE IF EXISTS history')
    cursor.execute('DROP TABLE IF EXISTS users')
    
    # Create users table
    cursor.execute('''
        CREATE TABLE users (
            id INT AUTO_INCREMENT PRIMARY KEY,
            name VARCHAR(100) NOT NULL,
            city VARCHAR(100) NOT NULL
        )
    ''')
    
    # Create history table with foreign key to users
    cursor.execute('''
        CREATE TABLE history (
            id INT AUTO_INCREMENT PRIMARY KEY,
            user_id INT NOT NULL,
            symptoms TEXT NOT NULL,
            conditions TEXT NOT NULL,
            self_care TEXT,
            timestamp DATETIME DEFAULT CURRENT_TIMESTAMP,
            FOREIGN KEY (user_id) REFERENCES users(id) ON DELETE CASCADE
        )
    ''')
    
    conn.commit()
    cursor.close()
    conn.close()


def get_or_create_user(name: str, city: str) -> int:
    conn = get_connection()
    cur = conn.cursor()

    cur.execute("SELECT id, city FROM users WHERE name = %s", (name,))
    row = cur.fetchone()
    if row:
        # Optionally update city if different here
        conn.close()
        return row[0]

    cur.execute("INSERT INTO users (name, city) VALUES (%s, %s)", (name, city))
    conn.commit()
    user_id = cur.lastrowid
    conn.close()
    return user_id


def get_user_city(user_id: int) -> str:
    conn = get_connection()
    cur = conn.cursor()
    cur.execute("SELECT city FROM users WHERE id = %s", (user_id,))
    row = cur.fetchone()
    conn.close()
    return row[0] if row else "Kigali"


def save_history(user_id: int, symptoms: str, conditions: str, self_care: str):
    conn = get_connection()
    cur = conn.cursor()
    cur.execute("""
        INSERT INTO history (user_id, symptoms, conditions, self_care)
        VALUES (%s, %s, %s, %s)
    """, (user_id, symptoms, conditions, self_care))
    conn.commit()
    conn.close()


def view_history(user_id: int):
    conn = get_connection()
    cur = conn.cursor()
    cur.execute("""
        SELECT symptoms, conditions, self_care, timestamp
        FROM history
        WHERE user_id = %s
        ORDER BY timestamp DESC
    """, (user_id,))
    rows = cur.fetchall()
    conn.close()
    return rows