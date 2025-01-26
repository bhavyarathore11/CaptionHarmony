import streamlit as st

def display_section():
    with st.container():
        st.markdown(
            '<div class="section-box"><h2>🌍 Translate Captions</h2><p>Translate captions into multiple languages.</p></div>',
            unsafe_allow_html=True,
        )
        st.text_input("Enter your caption for translation:")
