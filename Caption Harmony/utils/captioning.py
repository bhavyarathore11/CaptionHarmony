import streamlit as st
from PIL import Image
from transformers import VisionEncoderDecoderModel, ViTImageProcessor, AutoTokenizer

# Load Hugging Face model
model_name = "nlpconnect/vit-gpt2-image-captioning"
model = VisionEncoderDecoderModel.from_pretrained(model_name)
processor = ViTImageProcessor.from_pretrained(model_name)
tokenizer = AutoTokenizer.from_pretrained(model_name)

def display_section():
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
