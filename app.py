import streamlit as st

st.set_page_config(
    page_title="ML Streamlit App",
    layout="wide"
)

st.sidebar.title("Navigation")
st.sidebar.info("Use the pages on the left")

st.title("🚀 ML Streamlit Web App")
st.write("""
Welcome to a **complete Streamlit web application**.

Features:
- Multi-page navigation
- Clean backend structure
- ML inference
- Caching & performance
""")
