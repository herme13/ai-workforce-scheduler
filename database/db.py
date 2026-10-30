import sqlite3


DB_NAME = "scheduler.db"

def create_tables():

    conn = get_connection()

    cursor = conn.cursor()

    cursor.execute(
        """
        CREATE TABLE IF NOT EXISTS bookings (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            customer TEXT,
            lesson_date TEXT,
            lesson_time TEXT,
            students INTEGER,
            instructor TEXT,
            status TEXT
        )
        """
    )

    conn.commit()

    conn.close()
    
def get_connection():

    return sqlite3.connect(
        DB_NAME,
        check_same_thread=False
    )