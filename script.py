import streamlit as st
import pickle
import numpy as np

# Load your model (replace 'model.pkl' with your actual model file)
with open('ui.pckl', 'rb') as file:
    model = pickle.load(file)

# Define a function to make predictions
def predict_language(text):
    prediction = model.predict([text])
    return prediction[0]


# Streamlit App
st.title("Language Detection App")


user_input = st.text_area("Enter text to detect language:")

if st.button("Detect Language"):
    result = predict_language(user_input)
    st.write(f"Predicted Language: {result}")

