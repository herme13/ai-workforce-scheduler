import streamlit as st
import pandas as pd

from components.tables import render_dataframe
from services.database import (insert_booking, delete_booking, update_booking, delete_calendar_events_by_customer)

def show(bookings):

    st.title("📥 Booking Inbox")
    render_dataframe(bookings)
    # ==== TEMPORARAY DEBUG
    #st.write(bookings.columns.tolist())
    
    st.subheader("✅ New Booking")
    # variables
    customer = st.text_input("Customer Name")
    lesson_date = st.date_input("Lesson Date")
    lesson_time = st.time_input("Lesson Time")
    students = st.number_input("Students", min_value=1, value=1)

    if st.button("Create Booking"):
        if not customer.strip():
            st.error("Customer name is required.")
        else:

            formatted_date = (
            lesson_date.strftime("%b %d, %Y")
            .replace(" 0", " ")
            )

            formatted_time = (
            lesson_time.strftime("%I:%M %p")
            .lstrip("0")
            )

            duplicate_booking = (
            (bookings["Customer"] == customer)
            &
            (bookings["Date"] == formatted_date)
            &
            (bookings["Time"] == formatted_time)).any()

            if duplicate_booking:
                st.warning("This booking already exists.")
            else:  
                #======DATA BASE FUNCTION====
                insert_booking( # Insersert SQlite > Rerun > Reload Database (One source of truth)
                    customer,
                    formatted_date,
                    formatted_time,
                    students,
                    "Unassigned",
                    "Pending")
                st.success("Booking Created")
                st.rerun()

    with st.expander("View Booking Details"):

        st.json({
            "customer": customer,
            "date": str(lesson_date),
            "time": str(lesson_time),
            "students": students,
        })
    
    st.subheader("✏️ Edit Booking")
    if not bookings.empty:

        selected_id = st.selectbox(
        "Select Booking ID",
        bookings["Booking ID"],
        key="edit_booking_id")

        selected_booking = bookings[bookings["Booking ID"] == selected_id].iloc[0] 
        st.write(selected_booking)

        edit_customer = st.text_input(
            "Customer",
            value=selected_booking["Customer"],
            key="edit_customer")

        edit_students = st.number_input(
            "Students",
            min_value=1,
            value=int(selected_booking["Students"]),
            key="edit_students")

        if st.button("Save Changes"):
            st.write("Selected ID:", selected_id)
            st.write("Updated Customer:", edit_customer)
            st.write("Updated Students:", edit_students)

            update_booking(
                selected_id,
                edit_customer,
                selected_booking["Date"],
                selected_booking["Time"],
                edit_students)

            st.success("Booking Updated")
            st.rerun()
        
        with st.expander("Edit Booking Details"):
            # Instead of multiple st.write() calls:
            st.json({
                "Booking ID": selected_booking['Booking ID'],
                "Date": selected_booking['Date'],
                "Time": selected_booking['Time'],
                "Instructor": selected_booking['Instructor'],
                "Status": selected_booking['Status']
                })
            
    st.subheader("❌Delete Booking")
    if not bookings.empty:

        booking_to_delete = st.selectbox("Select Booking To Delete", bookings["Customer"])

        if st.button("🗑 Delete Booking"):

            delete_booking(booking_to_delete)
            delete_calendar_events_by_customer(booking_to_delete)
            st.success(f"{booking_to_delete} deleted.")

            st.rerun()

 
            
