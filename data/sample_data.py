import pandas as pd

def get_bookings():

    return pd.DataFrame([
        {
            "Booking ID": 1,
            "Customer": "Sarah Jones",
            "Status": "Pending",
            "Instructor": "Unassigned", # Dataframe columns must match
            "Date": "Nov 15, 2026",
            "Time": "10:00 AM",
            "Students": 3
            
            

        },
        {
            "Booking ID": 2,
            "Customer": "John Smith",
            "Status": "Assigned",
            "Instructor": "Unassigned",
            "Date": "Nov 17, 2026",
            "Time": "1:00 PM",
            "Students": 2
            
            
        },
        {
            "Booking ID": 3,
            "Customer": "Ashley Thompson",
            "Status": "Pending",
            "Instructor": "Unassigned",
            "Date": "Nov 30, 2026",
            "Time": "9:00 AM",
            "Students": 2
        }
            

    ])

def get_instructors():

    return pd.DataFrame([
        {"Instructor": "Mike", "Available": True},
        {"Instructor": "Michelle", "Available": True},
        {"Instructor": "Alex", "Available": True}
    ])

def get_calendar_events():

    return pd.DataFrame([
        {
            "Instructor": "Alex",
            "Customer": "John Smith",
            "Date": "Nov 15, 2026",
            "Time": "1:00 PM"
        }
    ])