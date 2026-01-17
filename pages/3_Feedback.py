import streamlit as st
import pandas as pd
import os

st.title("📝 Feedback Management")
st.write("Manage entries stored in the AI's short-term memory.")

if os.path.exists('feedback_log.csv'):
    df = pd.read_csv('feedback_log.csv', names=['Resume Content', 'Corrected Label'])
    st.dataframe(df, use_container_width=True)
    
    if st.button("Purge AI Memory"):
        os.remove('feedback_log.csv')
        st.warning("Memory cleared.")
        st.rerun()
else:
    st.success("No feedback entries found.")