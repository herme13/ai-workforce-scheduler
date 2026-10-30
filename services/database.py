import sqlite3
import pandas as pd

DATABASE_NAME = "scheduler.db"


def get_connection():

    conn = sqlite3.connect(
        DATABASE_NAME,
        check_same_thread=False
    )

    conn.execute(
        "PRAGMA foreign_keys = ON"
    )

    return conn


def initialize_database():

    conn = get_connection()

    cursor = conn.cursor()

    # -------------------------
    # BOOKINGS
    # -------------------------

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS bookings (
            id INTEGER PRIMARY KEY AUTOINCREMENT,

            customer TEXT NOT NULL,

            date TEXT NOT NULL,

            time TEXT NOT NULL,

            students INTEGER NOT NULL,

            instructor TEXT DEFAULT 'Unassigned',

            status TEXT DEFAULT 'Pending'
        )
    """)

    # -------------------------
    # CALENDAR EVENTS
    # -------------------------

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS calendar_events (
            id INTEGER PRIMARY KEY AUTOINCREMENT,

            booking_id INTEGER NOT NULL,

            instructor TEXT NOT NULL,

            customer TEXT NOT NULL,

            date TEXT NOT NULL,

            time TEXT NOT NULL,

            FOREIGN KEY (booking_id)
                REFERENCES bookings(id)
                ON DELETE CASCADE
        )
    """)

    conn.commit()

    conn.close()

def show_tables():

    conn = get_connection()

    cursor = conn.cursor()

    cursor.execute(
        "SELECT name FROM sqlite_master WHERE type='table';"
    )

    tables = cursor.fetchall()

    conn.close()

    return tables

def insert_booking(customer, date, time, students, instructor, status):

    conn = get_connection()

    cursor = conn.cursor()

    cursor.execute(
        """
        INSERT INTO bookings (customer, date,time, students, instructor,status)
        VALUES (?, ?, ?, ?, ?, ?)
        """,( customer,date,time,students,instructor,status)
        )

    conn.commit()
    conn.close()

def get_all_bookings():

    conn = get_connection()

    query = """
    SELECT id, customer, date, time, students, instructor, status
    FROM bookings"""

    df = pd.read_sql_query(query, conn)

    conn.close()

    df.columns = [
        "Booking ID",
        "Customer",
        "Date",
        "Time",
        "Students",
        "Instructor",
        "Status"
    ]

    return df

def insert_calendar_event(booking_id,instructor,customer,date,time):

    conn = get_connection()

    cursor = conn.cursor()

    # Verify booking exists first

    cursor.execute(
        """
        SELECT id
        FROM bookings
        WHERE id = ?
        """,
        (booking_id,)
    )

    booking_exists = cursor.fetchone()

    if not booking_exists:

        conn.close()

        raise ValueError(
            f"Booking ID {booking_id} does not exist."
        )

    cursor.execute(
        """
        INSERT INTO calendar_events (
            booking_id,
            instructor,
            customer,
            date,
            time
        )
        VALUES (?, ?, ?, ?, ?)
        """,(
            booking_id,
            instructor,
            customer,
            date,
            time)
    )

    conn.commit()

    conn.close()


def get_calendar_events():

    conn = get_connection()

    query = """
    SELECT
        id,
        booking_id,
        instructor,
        customer,
        date,
        time
    FROM calendar_events
    """

    df = pd.read_sql_query(query,conn)

    conn.close()

    return df

def update_booking_assignment(customer, instructor):

    conn = get_connection()

    cursor = conn.cursor()

    cursor.execute(
        
        """
        UPDATE bookings
        SET instructor = ?, status = ?
        WHERE customer = ?
        """,(instructor,"Assigned", customer))

    conn.commit()

    conn.close()

def delete_booking(customer):

    conn = get_connection()

    cursor = conn.cursor()
    
    #QUERY
    cursor.execute("""
        DELETE FROM bookings
        WHERE customer = ?""", (customer,))

    conn.commit()

    conn.close()

def update_booking(booking_id,customer,date,time,students):

    conn = get_connection()

    cursor = conn.cursor()
    print("UPDATE:",booking_id,customer,date,time,students)
    cursor.execute("""
        UPDATE bookings
        SET 
            customer = ?, 
            date = ?, 
            time = ?, 
            students = ?
        WHERE id = ?
        """,(customer,date,time,students,booking_id)
        )
    conn.commit()
    conn.close()

def show_schema(table_name):

    conn = get_connection()

    cursor = conn.cursor()

    cursor.execute(f"PRAGMA table_info({table_name})")

    schema = cursor.fetchall()

    conn.close()

    return schema

def delete_calendar_events_by_customer(customer):

    conn = get_connection()

    cursor = conn.cursor()

    cursor.execute(
        """
        DELETE FROM calendar_events
        WHERE customer = ?
        """,(customer,)) # SQLite wants a tuple (,) leave the comma

    conn.commit()

    conn.close()
