import streamlit as st
import pandas as pd
import plotly.express as px
import os

st.set_page_config(page_title="Model Analytics", layout="wide")
st.title("📊 Intelligence & Memory Dashboard")

# --- BASE DATASET STATS ---
try:
    # Use the Zipped Master Dataset
    df_main = pd.read_csv('Dataset/Master_Merged_Dataset.zip')
    st.subheader("Industry Distribution (Base Model)")
    top_20 = df_main['Category'].value_counts().head(20).reset_index()
    fig = px.bar(top_20, x='count', y='Category', orientation='h', color='count', color_continuous_scale='Blues')
    st.plotly_chart(fig, use_container_width=True)
except Exception as e:
    st.info("Run train_model.py first to generate the Master_Merged_Dataset.zip.")

st.divider()

# --- REVIEW MEMORY STATS ---
if os.path.exists('feedback_log.csv'):
    df_mem = pd.read_csv('feedback_log.csv', names=['Resume', 'Category'])
    st.subheader("🧠 Self-Learning Stats")
    st.metric("Corrections Stored", len(df_mem))
    fig_mem = px.pie(df_mem, names='Category', title="Memory Distribution", hole=0.3)
    st.plotly_chart(fig_mem, use_container_width=True)