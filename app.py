import streamlit as st
from PIL import Image, ImageEnhance
from io import BytesIO


st.set_page_config(page_title="Simple Image Enhancer",layout="centered")

st.title("🎨 Simple Color Manipulation Website")
st.write("Upload an image and adjust its brightness, contrast, sharpness, or color easily!")


uploaded_file = st.file_uploader("📤 Upload an Image", type=["jpg", "jpeg", "png"])

if uploaded_file:
    
    img = Image.open(uploaded_file).convert("RGB")
    st.image(img, caption="Original Image", use_container_width=True)


    st.subheader(" Enhancement Controls")
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

    buf = BytesIO()
    img.save(buf, format="PNG")
    byte_im = buf.getvalue()

    st.download_button(
        label="💾 Download Enhanced Image",
        data=byte_im,
        file_name="enhanced_image.png",
        mime="image/png"
    )

else:
    st.info("Please upload an image to get started!")


