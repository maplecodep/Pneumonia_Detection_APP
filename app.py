# app.py

import streamlit as st
import requests
import base64
import json
import os

# Set the AWS API endpoint URL as an environment variable
api_endpoint = os.getenv("AWS_API_ENDPOINT")

if not api_gateway_endpoint:
    st.error("AWS_API_ENDPOINT environment variable not set.")
    st.stop()

st.title("X-ray Pneumonia Detection App")

uploaded_file = st.file_uploader("Choose an X-ray image...", type="jpg")

if uploaded_file is not None:
    st.image(uploaded_file, caption="Uploaded X-ray.", use_column_width=True)
    st.write("")
    st.write("Classifying...")
    
    image_data = base64.b64encode(uploaded_file.read()).decode('utf-8')
    payload = {
        'image': image_data
    }
    
    # Send image data to AWS API endpoint
    response = requests.post(api_endpoint, json=payload)
    
    # Display the result
    result = response.json()
    st.write("Result:", result)
