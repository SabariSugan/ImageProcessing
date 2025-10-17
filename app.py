import streamlit as st
from PIL import Image, ImageEnhance

st.set_page_config(page_title="Simple Color Manipulator", page_icon="🎨", layout="centered")

st.title("🎨 Simple Color Manipulation Website")

uploaded_file = st.file_uploader("Upload an Image", type=["jpg", "jpeg", "png"])

if uploaded_file:
    img = Image.open(uploaded_file)
    st.image(img, caption="Original Image", use_container_width=True)

    st.subheader("Enhancement Controls")

    brightness = st.slider("Brightness", 0.5, 3.0, 1.0)
    contrast = st.slider("Contrast", 0.5, 3.0, 1.0)
    sharpness = st.slider("Sharpness", 0.5, 3.0, 1.0)
    color = st.slider("Color", 0.5, 3.0, 1.0)

    enhancer = ImageEnhance.Brightness(img)
    img = enhancer.enhance(brightness)

    enhancer = ImageEnhance.Contrast(img)
    img = enhancer.enhance(contrast)

    enhancer = ImageEnhance.Sharpness(img)
    img = enhancer.enhance(sharpness)

    enhancer = ImageEnhance.Color(img)
    img = enhancer.enhance(color)

    st.image(img, caption="Enhanced Image", use_container_width=True)

    st.download_button("Download Enhanced Image", img.tobytes(), "enhanced_image.png")

else:
    st.info("Upload an image to begin!")
