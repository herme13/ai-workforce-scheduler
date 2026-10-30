import streamlit as st
from data.sample_data import (get_bookings, get_instructors, get_calendar_events)
from pages import (dashboard, bookings, instructors, calendar, logs)
from services.database import (initialize_database, get_all_bookings, get_calendar_events)
from services.database import (show_tables, show_schema)
from database.db import create_tables
# ======TEMPORARY ADD IMPORT======
from services.database import get_all_bookings

# Initialize database when app starts
initialize_database()
# ========= DATABASE =========
calendar_df = get_calendar_events()
instructors_df = get_instructors()
bookings_df = get_all_bookings()


st.set_page_config(
    page_title="AI Workforce Scheduler",
    page_icon="💻",
    layout="wide"
)
# Create bookings table
create_tables()

# Instead of: - Booking -> Calendar -> Assignments (three separate datasets)
# We'll use: - Bookings -> Assignments -> Calendar Events (all backed by Session State)

# SQLite becomes the source of truth.
# Current: Bookings Created -> Session State -> Dashboard
# Target: SQLite -> Session State -> Dashboard 

#=====SESSION STATES=====
# FROM SAMPLE DATA
# First startup: Database Empty -> Load Sample Data (we update see below)
#if "bookings" not in st.session_state: 
   #st.session_state.bookings = get_bookings()
#bookings_df = st.session_state.bookings

#==== NEW BOOKING FLOW====
#database_bookings = get_all_bookings() # SQLite > get_all_bookings() > bookding_df > Dashboard, Bookings, Instructors, Calendar

###if database_bookings.empty:
###    bookings_df = get_bookings() # sample_date
##else:
###    bookings_df = database_bookings
# ===========================================
# FROM SQLite 
#if "bookings" not in st.session_state: #Future startup: Database Contains Bookings -> Load Bookings fromSQLite
    #database_bookings = get_all_bookings()
   # if database_bookings.empty:
        #st.session_state.bookings = get_bookings() # Just stop using: because of sample_data.py + SQLite , you want : SQLite > bookings_df > Everything Else
    #else:
        #st.session_state.bookings = database_bookings

#===KEEP=== (DELETED)
# "calendar_events" not in st.session_state:
    #st.session_state.calendar_events = get_calendar_events()
# this will be changed to match 'bookings_df' syntax WHY? because every re-run your newly created events disappers (you dont want that)
# Was: calendar_df = get_calendar_events()
#calendar_df = st.session_state.calendar_events
# ===============



st.sidebar.title(":🗺: AI Workforce Scheduler")

st.sidebar.caption(":🖥: Business Workflow Automation")

st.sidebar.divider()

tab1, tab2, tab3, tab4, tab5 = st.tabs(
    [
        "Dashboard",
        "Bookings",
        "Instructors",
        "Calendar",
        "Logs",
    ]
)

with tab1:
    dashboard.show(bookings_df,
                   calendar_df)

with tab2:
    bookings.show(bookings_df,
                  )

with tab3:
    instructors.show(
        bookings_df,
        instructors_df
    )

with tab4:
    calendar.show(calendar_df)

with tab5:
    logs.show()

# ======TEMPORARY ADD (DEBUGGING REAL DATA)======
st.write("SQLite Database",get_all_bookings()) # you can remove
st.write("SQLite Calendar Events",get_calendar_events())
#st.write("SQLite SHOW TABLES", show_tables())
#st.write("SQLite SHOW SCHEMA",show_schema("bookings"))
#st.write("Booking Columns", bookings_df.columns.tolist())