# clinics.py

from mysql.connector import Error
from database_connection import HealthSystem

class ClinicManager:
    def __init__(self):
        self.db = HealthSystem()
        self.connection = self.db.connection

    def add_clinic(self, name, city, distance_km):
        """Add a new clinic to the database."""
        try:
            cursor = self.connection.cursor()
            query = "INSERT INTO clinics (name, city, distance_km) VALUES (%s, %s, %s)"
            cursor.execute(query, (name, city, distance_km))
            self.connection.commit()
            cursor.close()
            print("[SUCCESS] Clinic '{}' added successfully.".format(name))
        except Error as e:
            print("[ERROR] Failed to add clinic:", e)

    def list_all_clinics(self):
        """Fetch and print all clinics from the database."""
        try:
            cursor = self.connection.cursor()
            cursor.execute("SELECT id, name, city, distance_km FROM clinics")
            rows = cursor.fetchall()
            cursor.close()

            if not rows:
                print("[INFO] No clinics found.")
                return

            print("\nList of Clinics:")
            for row in rows:
                print("ID: {}, Name: {}, City: {}, Distance: {} km".format(row[0], row[1], row[2], row[3]))
        except Error as e:
            print("[ERROR] Failed to fetch clinics:", e)

    def find_clinics_by_city(self, city):
        """Find and print clinics in a given city."""
        try:
            cursor = self.connection.cursor()
            cursor.execute("SELECT name, distance_km FROM clinics WHERE city = %s", (city,))
            rows = cursor.fetchall()
            cursor.close()

            if not rows:
                print("[INFO] No clinics found in '{}'.".format(city))
                return

            print("\nClinics in {}:".format(city))
            for row in rows:
                print("- {} ({} km away)".format(row[0], row[1]))
        except Error as e:
            print("[ERROR] Failed to search clinics:", e)

# Test functionality if run directly
if __name__ == "__main__":
    manager = ClinicManager()

    # Examples
    manager.add_clinic("Hope Medical Center", "Kigali", 5.2)
    manager.add_clinic("Bright Health Clinic", "Huye", 12.7)
    manager.add_clinic("Nobel Health Center", "Musanze", 7)
    manager.add_clinic("Polyclinique", "Nyagatare", 4.8)

    manager.list_all_clinics()
    manager.find_clinics_by_city("Kigali")

