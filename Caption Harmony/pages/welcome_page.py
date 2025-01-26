import streamlit as st
from styles.custom_css import CSS_STYLE

def display():
    # Apply styles
    st.markdown(
        CSS_STYLE.format(
            bg_image="https://media.istockphoto.com/id/1195616529/vector/white-studio-background-vector-template.jpg?s=612x612&w=0&k=20&c=tJvHZRmJxzIiQFio5b2vUgrooArpN8Q7xi-yYkLOWzk="
        ),
        unsafe_allow_html=True,
    )

    # Welcome page content
    st.markdown(
        """
        <div style="text-align: center; margin-top: 15%; color: white;">
            <h1>Welcome to</h1>
            <h2>Caption Harmony & Music Recommender 🎵📸</h2>
            <p style="font-size: 18px;">
                An AI-powered tool to create engaging captions, generate artistic descriptions, 
                discover relevant hashtags, and recommend music tailored to your mood.
            </p>
        </div>
        """,
        unsafe_allow_html=True,
    )
    if st.button("Enter the Application"):
        st.session_state.page = "main"
