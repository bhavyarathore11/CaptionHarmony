import streamlit as st
from PIL import Image
from transformers import VisionEncoderDecoderModel, ViTImageProcessor, AutoTokenizer, pipeline
from transformers import MarianMTModel, MarianTokenizer

# Load Hugging Face model for captioning
model_name = "nlpconnect/vit-gpt2-image-captioning"
model = VisionEncoderDecoderModel.from_pretrained(model_name)
processor = ViTImageProcessor.from_pretrained(model_name)
tokenizer = AutoTokenizer.from_pretrained(model_name)

# Artistic description generation pipeline (GPT-2)
artistic_generator = pipeline("text-generation", model="gpt2")

# Translation model for multilingual captions
translation_model_name = "Helsinki-NLP/opus-mt-en-ROMANCE"
translator = MarianMTModel.from_pretrained(translation_model_name)
translation_tokenizer = MarianTokenizer.from_pretrained(translation_model_name)

# Streamlit app configuration
st.set_page_config(page_title="Caption Harmony & Music Recommender", page_icon="🎵📸", layout="wide")

# Page state management
if "page" not in st.session_state:
    st.session_state.page = "welcome"

# CSS styles with improved background image handling
CSS_STYLE = """
     <style>
    body {{
        background-image: url('{bg_image}');
        background-size: cover;
        background-attachment: fixed;
        margin: 0;
        padding: 0;
        height: 100vh;
    }}
    .stApp {{
        background-color: rgba(0, 0, 0, 0); /* Transparent background for app */
        background-image: url('{bg_image}'); /* Fallback for app background */
        background-size: cover;
        background-attachment: fixed;
    }}
    .block-container {{
        background-color: rgba(0, 0, 0, 0); /* Transparent background for block container */
        padding: 0 1rem;
    }}
    h1, h2, h3, p {{
        color: white;
        text-shadow: 2px 2px 8px rgba(0, 0, 0, 0.7);
        text-align: center;
    }}
    .stButton > button {{
        background-color: #ff6f61;
        color: white;
        border: none;
        padding: 10px 20px;
        font-size: 18px;
        font-weight: bold;
        border-radius: 20px;
        transition: all 0.3s ease;
    }}
    .stButton > button:hover {{
        background-color: #ff856b;
        box-shadow: 0px 4px 15px rgba(255, 111, 97, 0.4);
        transform: scale(1.05);
    }}
    .section-box {{
        background-color: rgba(0, 0, 0, 0.6);
        padding: 20px;
        border-radius: 10px;
        margin-bottom: 20px;
        box-shadow: 0 4px 15px rgba(0, 0, 0, 0.2);
        transition: all 0.3s ease;
    }}
    .footer {{
        text-align: center;
        color: white;
        margin-top: 30px;
        font-size: 14px;
    }}
    </style>
"""

# Applying the updated CSS
background_image = (
    "https://media.istockphoto.com/id/1195616529/vector/white-studio-background-vector-template.jpg?s=612x612&w=0&k=20&c=tJvHZRmJxzIiQFio5b2vUgrooArpN8Q7xi-yYkLOWzk="
    if st.session_state.page == "welcome"
    else "https://c4.wallpaperflare.com/wallpaper/445/123/761/soft-gradient-solid-color-gradient-hd-wallpaper-preview.jpg"
)
st.markdown(CSS_STYLE.format(bg_image=background_image), unsafe_allow_html=True)

# Welcome page
if st.session_state.page == "welcome":
    st.markdown(
        f"""
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

# Main application page
elif st.session_state.page == "main":
    st.markdown(
        """
        <div style="text-align: center; margin-bottom: 40px; color: white;">
            <h1>🎵📸 Caption Harmony & Music Recommender</h1>
            <p style="font-size: 18px;">Explore our sections to enhance your social media content and discover new music.</p>
        </div>
        """,
        unsafe_allow_html=True,
    )

    # Section: Post Caption
    with st.container():
        st.markdown(
            '<div class="section-box"><h2>📝 Generate Captions</h2><p>Upload an image and get a perfect caption for your post.</p></div>',
            unsafe_allow_html=True,
        )
        uploaded_image = st.file_uploader("Upload an image (JPG/PNG)", type=["jpg", "png"])
        if uploaded_image:
            image = Image.open(uploaded_image)
            st.image(image, caption="Uploaded Image", use_column_width=True)
            image_tensor = processor(images=image, return_tensors="pt").pixel_values
            outputs = model.generate(image_tensor)
            caption = tokenizer.decode(outputs[0], skip_special_tokens=True)
            st.success(f"Generated Caption: {caption}")

    # Section: Artistic Description
    with st.container():
        st.markdown(
            '<div class="section-box"><h2>🎨 Artistic Description</h2><p>Generate a creative description for your image.</p></div>',
            unsafe_allow_html=True,
        )
        if uploaded_image:
            artistic_description = artistic_generator(
                f"Create an artistic description of the following caption: {caption}", max_length=100
            )[0]["generated_text"]
            st.write(artistic_description)

    # Section: Hashtags
    with st.container():
        st.markdown(
            '<div class="section-box"><h2>🔖 Hashtags</h2><p>Get the most relevant hashtags for your caption.</p></div>',
            unsafe_allow_html=True,
        )
        if uploaded_image:
            keywords = caption.split()[:10]
            hashtags = ["#" + keyword.lower() for keyword in keywords]
            st.write(", ".join(hashtags))

    # Section: Multilingual Captions
    with st.container():
        st.markdown(
            '<div class="section-box"><h2>🌐 Multilingual Captions</h2><p>Translate your caption into different languages.</p></div>',
            unsafe_allow_html=True,
        )
        if uploaded_image:
            selected_language = st.selectbox("Select a language", ["French", "Spanish", "German"])
            language_map = {"French": "fr", "Spanish": "es", "German": "de"}
            translated = translator.generate(
                **translation_tokenizer(caption, return_tensors="pt", padding=True)
            )
            translated_caption = translation_tokenizer.decode(translated[0], skip_special_tokens=True)
            st.write(f"**{selected_language}**: {translated_caption}")

    # Section: Music Recommendation
    with st.container():
        st.markdown(
            '<div class="section-box"><h2>🎶 Music Recommendations</h2><p>Discover personalized music based on your mood or preferences.</p></div>',
            unsafe_allow_html=True,
        )
        mood = st.selectbox("Select your mood", ["Happy", "Sad", "Energetic", "Relaxed"])
        recommendations = {
            "Happy": ["Happy by Pharrell Williams", "Walking on Sunshine by Katrina and the Waves"],
            "Sad": ["Someone Like You by Adele", "Fix You by Coldplay"],
            "Energetic": ["Eye of the Tiger by Survivor", "Lose Yourself by Eminem"],
            "Relaxed": ["Weightless by Marconi Union", "Clair de Lune by Debussy"],
        }
        st.write("Here are some songs for your mood:")
        st.write("\n".join(recommendations[mood]))

    # Section: Back to Welcome Page
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
