import streamlit as st
from pages import welcome_page, main_page

# Streamlit app configuration
st.set_page_config(page_title="Caption Harmony & Music Recommender", page_icon="🎵📸", layout="wide")

# Page state management
if "page" not in st.session_state:
    st.session_state.page = "welcome"

# Navigate between pages
if st.session_state.page == "welcome":
    welcome_page.display()
elif st.session_state.page == "main":
    main_page.display()
