import streamlit as st
from styles.custom_css import CSS_STYLE
from utils import captioning, artistic, hashtags, translation, music

def display():
    # Apply styles
    st.markdown(
        CSS_STYLE.format(
            bg_image="https://c4.wallpaperflare.com/wallpaper/445/123/761/soft-gradient-solid-color-gradient-hd-wallpaper-preview.jpg"
        ),
        unsafe_allow_html=True,
    )

    # Main page header
    st.markdown(
        """
        <div style="text-align: center; margin-bottom: 40px; color: white;">
            <h1>🎵📸 Caption Harmony & Music Recommender</h1>
            <p style="font-size: 18px;">Explore our sections to enhance your social media content and discover new music.</p>
        </div>
        """,
        unsafe_allow_html=True,
    )

    # Sections
    captioning.display_section()
    artistic.display_section()
    hashtags.display_section()
    translation.display_section()
    music.display_section()

    # Back to Welcome Page
    if st.button("Back to Welcome Page"):
        st.session_state.page = "welcome"

    # Footer
    st.markdown(
        """
        <div class="footer">
            <p>Made with ❤️ using Streamlit and Hugging Face Transformers</p>
        </div>
        """,
        unsafe_allow_html=True,
    )
