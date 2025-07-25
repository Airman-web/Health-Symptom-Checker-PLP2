-- Database schema for the application: helps us define tables(symptoms, conditions, diseases, clinics) and their relationships.
CREATE TABLE IF NOT EXISTS symptoms (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    systom TEXT NOT NULL
);

CREATE TABLE IF NOT EXISTS conditions (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    condition_name TEXT NOT NULL,
    self-care_tips TEXT,
);

CREATE TABLE IF NOT EXISTS symptom_condition (
    symptom_id INTEGER,
    condition_id INTEGER,
    FOREIGN KEY (symptom_id) REFERENCES symptoms(id),
    FOREIGN KEY (condition_id) REFERENCES conditions(id)

);

CREATE TABLE IF NOT EXISTS clinics (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    clinic_name TEXT NOT NULL,
    location_name TEXT NOT NULL,

);