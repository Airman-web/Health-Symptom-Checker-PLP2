import mysql.connector

def test_connection():
    try:
        conn = mysql.connector.connect(
            host="mysql-3a5d805c-alustudent-721c.f.aivencloud.com",
            port=22850,
            user="avnadmin",
            password="AVNS_4BIPxiawsylQ3_RxxoX",
            database="defaultdb"
        )
        if conn.is_connected():
            print("✅ Connection to Aiven MySQL was successful!")
            cursor = conn.cursor()
            cursor.execute("SHOW TABLES;")
            tables = cursor.fetchall()
            print("📋 Existing tables:")
            for table in tables:
                print(f" - {table[0]}")
        else:
            print("❌ Failed to connect.")

    except mysql.connector.Error as err:
        print("❌ MySQL error:", err)

    finally:
        if 'conn' in locals() and conn.is_connected():
            conn.close()

test_connection()
