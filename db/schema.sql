CREATE TABLE IF NOT EXISTS users (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(100) NOT NULL,
    age INT NOT NULL,
    gender VARCHAR(10) NOT NULL,
    phone VARCHAR(20),
    language VARCHAR(5) DEFAULT 'en'
);

CREATE TABLE IF NOT EXISTS clinics (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(100) NOT NULL,
    district VARCHAR(100) NOT NULL,
    sector VARCHAR(100) NOT NULL
);

CREATE TABLE IF NOT EXISTS history (
    id INT AUTO_INCREMENT PRIMARY KEY,
    user_id INT NOT NULL,
    symptom TEXT NOT NULL,
    prediction TEXT NOT NULL,
    advice TEXT,
    clinic_id INT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (user_id) REFERENCES users(id),
    FOREIGN KEY (clinic_id) REFERENCES clinics(id)
);
