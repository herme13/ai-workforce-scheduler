import streamlit as st

def render_metrics(metrics):

    col1, col2, col3 = st.columns(3)

    with col1:
        st.metric("📥 Incoming Requests", metrics["total"])

    with col2:
        st.metric("✅ Lessons Scheduled", metrics["assigned"])

    with col3:
        st.metric("⏳ Awaiting Assignment", metrics["pending"])