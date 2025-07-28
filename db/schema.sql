-- db/schema.sql

DROP TABLE IF EXISTS users;
DROP TABLE IF EXISTS symptoms_conditions;
DROP TABLE IF EXISTS clinics;
DROP TABLE IF EXISTS history;

CREATE TABLE IF NOT EXISTS users (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    city TEXT NOT NULL
);

CREATE TABLE IF NOT EXISTS symptoms_conditions (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    symptom TEXT NOT NULL,
    condition TEXT NOT NULL,
    self_care TEXT
);

CREATE TABLE IF NOT EXISTS clinics (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    doctor TEXT NOT NULL,
    contact TEXT NOT NULL,
    city TEXT NOT NULL
);

CREATE TABLE IF NOT EXISTS history (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    user_id INTEGER NOT NULL,
    symptoms TEXT,
    conditions TEXT,
    self_care TEXT,
    timestamp DATETIME DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (user_id) REFERENCES users (id)
);
