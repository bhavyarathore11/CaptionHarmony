import streamlit as st

def display_section():
    with st.container():
        st.markdown(
            '<div class="section-box"><h2>#️⃣ Generate Hashtags</h2><p>Generate hashtags for your content.</p></div>',
            unsafe_allow_html=True,
        )
        st.text_input("Enter keywords or caption to generate hashtags:")
