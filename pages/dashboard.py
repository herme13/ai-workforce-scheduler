import streamlit as st

from services.metrics_service import booking_metrics
from components.metrics import render_metrics
from components.tables import render_dataframe


def show(bookings, calendar_events):

    st.title("AI Workforce Scheduling Platform")

    st.markdown("""
    ### Automated Scheduling & Workforce Coordination

    Manage bookings, assign instructors, monitor scheduling activity,
    and prepare for AI-powered workforce automation.
    """)

    st.divider()

    # ------------------------------------
    # EXISTING BOOKING METRICS
    # ------------------------------------

    metrics = booking_metrics(bookings)
    render_metrics(metrics)
        
    # ------------------------------------
    # BOOKING STATUS CHART
    # ------------------------------------

    st.subheader("Booking Status")
    status_counts = (bookings["Status"].value_counts())
    st.bar_chart(status_counts, color="green")
    
    st.divider()

    st.subheader("📅 Upcoming Lessons")
    if not calendar_events.empty:

        st.dataframe(
            calendar_events,
            use_container_width=True
            )
    else:
        st.info(
        "No lessons have been scheduled yet.")
    st.divider()
    
    # ------------------------------------
    # INSTRUCTOR ANALYTICS
    # ------------------------------------

    assigned_bookings = bookings[
        bookings["Instructor"] != "Unassigned"
    ]
    
    #st.write("Dashboard Bookings")
    #st.dataframe(bookings)
    active_instructors = 0
    most_active_instructor = "None"
    lesson_count = 0

    if not assigned_bookings.empty:

        instructor_counts = (assigned_bookings["Instructor"].value_counts())

        active_instructors = len(instructor_counts)

        most_active_instructor = (instructor_counts.idxmax())

        lesson_count = (instructor_counts.max())

    col1, col2 = st.columns(2)

    with col1:
        st.metric(
            "👨‍🏫 Active Instructors",
            active_instructors
        )

    with col2:
        st.metric(
            "🏆 Most Active Instructor",
            f"{most_active_instructor} ({lesson_count})"
        )
    st.divider()

    # ------------------------------------
    # BOOKINGS TABLE
    # ------------------------------------

    #st.subheader(" Current Bookings")
    #render_dataframe(bookings)

    