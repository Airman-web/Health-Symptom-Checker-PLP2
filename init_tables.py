from modules.history import init_db

if __name__ == "__main__":
    print("Initializing database tables...")
    try:
        init_db()
        print("✅ Database tables initialized successfully!")
    except Exception as e:
        print(f"❌ Error initializing database: {e}")
