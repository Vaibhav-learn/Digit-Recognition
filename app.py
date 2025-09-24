import streamlit as st
import numpy as np
import tensorflow as tf
from PIL import Image, ImageOps

# Load the trained model
model = tf.keras.models.load_model('best_model.h5')

st.title("🧠 Digit Recognition App")
st.write("Upload a 28x28 grayscale image of a digit (0–9) to get a prediction.")

uploaded_file = st.file_uploader("Choose an image...", type=["png", "jpg", "jpeg"])

if uploaded_file is not None:
    image = Image.open(uploaded_file).convert('L')  # Convert to grayscale
    image = ImageOps.invert(image)                  # Invert colors (white on black)
    image = image.resize((28, 28))                  # Resize to 28x28
    img_array = np.array(image) / 255.0             # Normalize pixel values
    img_array = img_array.reshape(1, 28, 28, 1)      # Reshape for model input

    st.image(image, caption="Uploaded Digit", width=150)
    prediction = model.predict(img_array)
    predicted_digit = np.argmax(prediction)

    st.success(f"Predicted Digit: **{predicted_digit}**")