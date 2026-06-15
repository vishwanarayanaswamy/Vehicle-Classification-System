import streamlit as st
import tensorflow as tf
import numpy as np
from PIL import Image

# Load model
model = tf.keras.models.load_model("best_model.keras")

# Class names
class_names = [
    "Auto Rickshaws",
    "Cycles",
    "Cars",
    "Motorcycles",
    "Planes",
    "Ships",
    "Trains"
]

st.title("🚗 Vehicle Classification System")

uploaded_file = st.file_uploader(
    "Upload Vehicle Image",
    type=["jpg","jpeg","png"]
)

if uploaded_file is not None:

    image = Image.open(uploaded_file)

    st.image(
        image,
        caption="Uploaded Image",
        use_container_width=True
    )

    img = image.resize((224,224))

    img_array = np.array(img)

    img_array = np.expand_dims(
        img_array,
        axis=0
    )

    prediction = model.predict(img_array)

    predicted_class = class_names[
        np.argmax(prediction)
    ]

    confidence = np.max(prediction) * 100

    st.success(
        f"Prediction: {predicted_class}"
    )

   