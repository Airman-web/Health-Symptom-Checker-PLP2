import mysql.connector
from mysql.connector import Error
from typing import Optional
import traceback


class HealthSystem:
    def __init__(self):
        self.connection: Optional[mysql.connector.connection_cext.CMySQLConnection] = None
        print("Starting HealthSystem...")

        self.connect_to_database()
        self.init_db()

    def connect_to_database(self) -> None:
        """Establish connection to the MySQL database"""
        try:
            self.connection = mysql.connector.connect(
                host='hacker1-alustudent-2f3d.f.aivencloud.com',
                port=18313,
                user='avnadmin',
                password='AVNS_VflP9EN1pLDf4T69IYY',
                database='defaultdb'
            )

            if self.connection.is_connected():
                print("Connected to the MySQL database successfully.")
        except Error:
            print("Failed to connect to the MySQL database:")
            traceback.print_exc()
            raise

    def init_db(self) -> None:
        """Create required tables if they don't exist"""
        try:
            cursor = self.connection.cursor()

            # Table: symptoms_conditions
            cursor.execute('''
                CREATE TABLE IF NOT EXISTS symptoms_conditions (
                    id INT AUTO_INCREMENT PRIMARY KEY,
                    symptom VARCHAR(100) NOT NULL,
                    `condition` VARCHAR(100) NOT NULL,
                    self_care TEXT
                )
            ''')

            # Table: clinics
            cursor.execute('''
                CREATE TABLE IF NOT EXISTS clinics (
                    id INT AUTO_INCREMENT PRIMARY KEY,
                    name VARCHAR(100) NOT NULL,
                    city VARCHAR(100) NOT NULL,
                    distance_km FLOAT
                )
            ''')

            # Table: history
            cursor.execute('''
                CREATE TABLE IF NOT EXISTS history (
                    id INT AUTO_INCREMENT PRIMARY KEY,
                    symptoms TEXT NOT NULL,
                    conditions TEXT NOT NULL,
                    timestamp DATETIME DEFAULT CURRENT_TIMESTAMP
                )
            ''')

            self.connection.commit()
            cursor.close()
            print("Tables created or verified successfully.")

        except Error:
            print("Error while creating tables:")
            traceback.print_exc()
            raise


# Run if script is executed directly
if __name__ == "__main__":
    HealthSystem()


