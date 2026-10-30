import streamlit as st
from datetime import datetime


def show():

    st.title("📝 Activity Logs")

    logs = [
        "Booking received",
        "Instructor assigned",
        "Calendar event created",
        "Confirmation sent"
    ]

    for log in logs:

        st.write(f"{datetime.now()} | {log}")