# modules/clinics.py
from db.database import get_connection

def get_clinic_by_city(city: str):
    conn = get_connection()
    cur = conn.cursor()
    cur.execute("""
        SELECT name, doctor, contact
        FROM clinics
        WHERE LOWER(city) = LOWER(?)
        ORDER BY RANDOM()
        LIMIT 1
    """, (city,))
    row = cur.fetchone()
    conn.close()
    return row

def get_random_clinic():
    conn = get_connection()
    cur = conn.cursor()
    cur.execute("SELECT name, doctor, contact FROM clinics ORDER BY RANDOM() LIMIT 1")
    row = cur.fetchone()
    conn.close()
    return row
