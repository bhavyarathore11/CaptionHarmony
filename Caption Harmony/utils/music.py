import streamlit as st

def display_section():
    with st.container():
        st.markdown(
            '<div class="section-box"><h2>🎵 Recommend Music</h2><p>Discover music tailored to your mood.</p></div>',
            unsafe_allow_html=True,
        )
        st.selectbox("Select your mood:", ["Happy", "Sad", "Energetic", "Relaxed"])
