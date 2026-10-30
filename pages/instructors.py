import streamlit as st
# to use pd.concat()
import pandas as pd
from services.scheduling_service import (get_available_instructors)
from services.database import (update_booking_assignment, insert_calendar_event)


def show(bookings, instructors):

    st.title("🤼 Instructors")

    st.dataframe(instructors, use_container_width=True)
    available = get_available_instructors(instructors)

    st.subheader("🔊 Available Instructors")
    st.dataframe(available)

    pending = bookings[bookings["Status"] == "Pending"]
    
    st.write("🔁Pending Bookings")
    st.write(pending)
    if not pending.empty:
        booking = st.selectbox("Select Customer Booking", pending["Customer"])
        instructor = st.selectbox("Assign Instructor", available["Instructor"])
        if st.button("Assign"):
            matching_rows = bookings[bookings["Customer"] == booking]
            if not matching_rows.empty:
                ###Why: We're removing old Session State code SQLite is already the source of truth. Matches the refactor we've been working toward.
                #booking_index = matching_rows.index[0]
                #st.session_state.bookings.loc[booking_index, "Status"] = "Assigned"
                #st.session_state.bookings.loc[booking_index,"Instructor"] = instructor 
                update_booking_assignment(booking, instructor)
                selected_booking = bookings[bookings["Customer"] == booking].iloc[0]
                booking_id = int(selected_booking["Booking ID"])

                st.write("Booking ID:", booking_id)
                st.write("Selected Booking:")
                st.write(selected_booking)

                insert_calendar_event(
                    booking_id,
                    instructor,
                    booking,
                    selected_booking["Date"],
                    selected_booking["Time"])
                
                ###WHY? Now this workflow exists: Booking Created-> Pending-> Assign Instructor-> Assigned-> Calendar Event Created
                #new_event = {
                    #"Instructor": instructor,
                    #"Customer": booking,
                    #"Date": st.session_state.bookings.loc[booking_index,"Date"],
                    #"Time": st.session_state.bookings.loc[booking_index,"Time"]
                    #}
                #st.session_state.calendar_events = pd.concat([st.session_state.calendar_events, pd.DataFrame([new_event])], ignore_index=True)

                st.success(f"{booking} assigned to {instructor}")
                st.rerun()

