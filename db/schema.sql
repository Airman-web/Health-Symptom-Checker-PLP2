-- db/schema.sql

-- Users table now stores city
CREATE TABLE IF NOT EXISTS users (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    city TEXT NOT NULL
);

CREATE TABLE IF NOT EXISTS history (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    user_id INTEGER NOT NULL,
    symptoms TEXT NOT NULL,
    conditions TEXT NOT NULL,
    self_care TEXT NOT NULL,
    timestamp DATETIME DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (user_id) REFERENCES users(id)
);

CREATE TABLE IF NOT EXISTS symptoms_conditions (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    symptom TEXT NOT NULL,
    condition TEXT NOT NULL,
    self_care TEXT NOT NULL
);

-- Add district & sector to better localize clinics inside Kigali
CREATE TABLE IF NOT EXISTS clinics (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    doctor TEXT NOT NULL,
    city TEXT NOT NULL,
    district TEXT NOT NULL,
    sector TEXT NOT NULL,
    contact TEXT
);
