# AI Workforce Scheduler

A workforce scheduling application built with Python, Streamlit, SQLite, and Pandas.

## `Overview`

This project simulates a real-world workforce scheduling platform.

    Users can:

- Create bookings
- Edit bookings
- Delete bookings
- Assign instructors
- Generate calendar events
- Track workforce activity through dashboard analytics
## Features
## `Booking Management`
- Create bookings
- Edit bookings
- Delete bookings
- Booking ID tracking
- Duplicate booking validation
## `Instructor Assignment`
- Assign instructors
- Track workload
- Update lesson status
## `Calendar Scheduling`
- Calendar event creation
- Event persistence
- Booking relationships
## `Dashboard`
- Lessons Scheduled
- Pending Assignments
- Active Instructors
- Most Active Instructor
- Upcoming Lessons
## `Technology Stack`
- Python
- Streamlit
- SQLite
- Pandas
## Database Design
### bookings table
Columnid > customer > date > time >students >instructor > status
### calendar_events
Columnid
booking_id
instructor
customer
date
time
### Architecture


SQLite
↓
get_all_bookings()
↓
bookings_df
↓
 
Dashboard
Bookings
Instructors
Calendar

# Future Enhancements
- Google Calendar Integration
- Gmail Integration
- AI Scheduling Agent
- Automated Notifications