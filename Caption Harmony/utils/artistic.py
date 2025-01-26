import streamlit as st

def display_section():
    with st.container():
        st.markdown(
            '<div class="section-box"><h2>🎨 Generate Artistic Descriptions</h2><p>Get creative descriptions for your images.</p></div>',
            unsafe_allow_html=True,
        )
        st.text_input("Enter your caption here:", placeholder="Describe your artistic vision...")
