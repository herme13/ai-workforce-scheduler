import streamlit as st


def show(calendar_events):

    st.title("📅 Calendar")

    st.dataframe(calendar_events, use_container_width=True)

    for _, row in calendar_events.iterrows():

        st.info(
            f"""
            Booking ID: {row['id']}
            Date: {row['date']}
            Time: {row['time']}
            Instructor: {row['instructor']}
            Customer: {row['customer']}
            """
        )
