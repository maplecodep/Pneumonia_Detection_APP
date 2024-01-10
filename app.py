# app.py

import streamlit as st
import requests
import base64
import json

# Set the AWS API endpoint URL as an environment variable
api_endpoint = "https://ferhbohwk5.execute-api.us-west-2.amazonaws.com/production"

st.title("X-ray Pneumonia Detection App")

uploaded_file = st.file_uploader("Choose an X-ray image...", type="jpg")

if uploaded_file is not None:
    st.image(uploaded_file, caption="Uploaded X-ray.", use_column_width=True)
    st.write("")
    st.write("Classifying...")

    # Send image data to AWS API endpoint
    response = requests.post(api_endpoint, files={"file": uploaded_file})
    
    # Display the result
    result = response.json()
    st.write("Result:", result)
