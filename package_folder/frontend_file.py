import streamlit as st
import requests
from PIL import Image
import io

st.title("Sign sense app")
st.write("Upload your image")

# File uploader widget
uploaded_file = st.file_uploader("Import your image", type=["jpg", "jpeg"])
# print(uploaded_file)
# Display the uploaded image
if uploaded_file is not None:
    image = Image.open(uploaded_file)
    img_bytes = io.BytesIO()
    image.save(img_bytes, format='JPEG')
    st.image(image, caption='Uploaded Image.', use_column_width=True)

    # Button to trigger prediction
    if st.button('Predict'):
        # Make API request
        predicted_letter = predict_letter(uploaded_file)
        st.write(f'Predicted Letter: {predicted_letter}')
