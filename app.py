import streamlit as st
from PIL import Image
from tensorflow.keras.preprocessing.image import load_img, img_to_array
import numpy as np
from tensorflow.keras.models import load_model
import os
import uuid

# Load the model safely
def load_model_safe(path):
    try:
        return load_model(path, compile=False)
    except Exception as e:
        st.error(f"Error loading model: {e}")
        return None

model = load_model_safe('./Model/BC.h5')

# Label mapping
lab = {0: 'AFRICAN CROWNED CRANE', 1: 'AFRICAN FIREFINCH', ...}  # Ensure this is complete

def processed_img(img_path):
    try:
        img = load_img(img_path, target_size=(224, 224))
        img = img_to_array(img)
        img = img / 255.0
        img = np.expand_dims(img, axis=0)
        answer = model.predict(img)
        y_class = answer.argmax(axis=-1)[0]
        res = lab[y_class]
        return res
    except Exception as e:
        st.error(f"Error processing image: {e}")
        return "Error"

def save_uploaded_file(uploaded_file):
    try:
        file_path = f'./upload_images/{uuid.uuid4().hex}_{uploaded_file.name}'
        with open(file_path, "wb") as f:
            f.write(uploaded_file.getbuffer())
        return file_path
    except Exception as e:
        st.error(f"Error saving file: {e}")
        return None

def run():
    st.set_page_config(
        page_icon="./meta/logo3.png",
        page_title="Bird Species Identification"
    )
    img1 = Image.open('./meta/logo3.png')
    img1 = img1.resize((210, 210))
    st.image(img1, use_column_width=False)
    st.markdown(
        '''<h1 style='text-align: right; color: #ffffff; margin-top:-180px;'>Bird Species Identification</h1>''',
        unsafe_allow_html=True)
    st.markdown(
        '''<h4 style='text-align: center; color: #d73b5c; margin-top:-130px;'>Data is based on "270 Bird Species"</h4>''',
        unsafe_allow_html=True)

    img_file = st.file_uploader("Choose an Image of Bird", type=["jpg", "png"])
    if img_file is not None:
        st.image(img_file, use_column_width=True)
        save_image_path = save_uploaded_file(img_file)
        if save_image_path:
            if st.button("Predict"):
                result = processed_img(save_image_path)
                st.success("Predicted Bird is: " + result)

if __name__ == "__main__":
    run()
