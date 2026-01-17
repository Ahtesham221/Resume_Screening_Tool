import streamlit as st

st.set_page_config(
    page_title="AI Resume Hub",
    page_icon="🚀",
    layout="wide"
)

st.title("🚀 Enterprise AI Resume Screening Hub")
st.subheader("Next-Gen Recruitment with Dynamic Self-Learning")

st.markdown("""
---
### 🌟 System Overview
This platform utilizes a **Hybrid AI Architecture**. It combines a static **KNN-Classifier** with a dynamic **Memory Layer** that learns from user corrections in real-time.

**Key Capabilities:**
* **Self-Learning:** The system remembers user feedback via its memory layer.
* **Universal Document Support:** Analyze `.pdf`, `.docx`, `.txt`, and images.
* **Real-time Analytics:** Explore the distribution of 100+ job categories.
---
""")

col1, col2, col3 = st.columns(3)
with col1:
    st.info("### 100+")
    st.write("**Job Categories**")
with col2:
    st.success("### 3,500+")
    st.write("**Training Samples**")
with col3:
    st.warning("### Hybrid AI")
    st.write("**Model + Memory**")

st.sidebar.success("Select a page above to get started.")
st.info("👈 **Get Started:** Use the sidebar to navigate to the **Screener** tool.")