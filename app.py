import streamlit as st
from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing import image
import numpy as np

# Load model
model = load_model('malaria_model.keras')

st.title("Malaria Cell Detection App")

file = st.file_uploader("Upload a Cell Image", type=['jpg', 'png'])
if file:
  img = image.load_img(file, target_size=(128, 128))
  img_array = np.expand_dims(image.img_to_array(img)/255.0, axis=0)
  pred = model.predict(img_array)[0][0]
  st.image(img, caption="Uploaded Cell", use_container_width=True)
  
  # Display prediction results
  if pred > 0.5:
    st.success("Uninfected Cell Detected")
  else:
    st.error("Infected Cell Detected")