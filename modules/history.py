# modules/history.py
from db.database import get_connection

def get_or_create_user(name: str, city: str):
    conn = get_connection()
    cur = conn.cursor()

    cur.execute("SELECT id, city FROM users WHERE name = ?", (name,))
    row = cur.fetchone()
    if row:
        # If the stored city is different, you could update it here if you want.
        conn.close()
        return row[0]

    cur.execute("INSERT INTO users (name, city) VALUES (?, ?)", (name, city))
    conn.commit()
    user_id = cur.lastrowid
    conn.close()
    return user_id

def get_user_city(user_id: int) -> str:
    conn = get_connection()
    cur = conn.cursor()
    cur.execute("SELECT city FROM users WHERE id = ?", (user_id,))
    row = cur.fetchone()
    conn.close()
    return row[0] if row else "Kigali"

def save_history(user_id, symptoms, conditions, self_care):
    conn = get_connection()
    cur = conn.cursor()
    cur.execute("""
        INSERT INTO history (user_id, symptoms, conditions, self_care)
        VALUES (?, ?, ?, ?)
    """, (user_id, symptoms, conditions, self_care))
    conn.commit()
    conn.close()

def view_history(user_id):
    conn = get_connection()
    cur = conn.cursor()
    cur.execute("""
        SELECT symptoms, conditions, self_care, timestamp
        FROM history
        WHERE user_id = ?
        ORDER BY timestamp DESC
    """, (user_id,))
    rows = cur.fetchall()
    conn.close()
    return rows
