
import streamlit as st
import joblib
import numpy as np
import pandas as pd

# Load the trained model
model = joblib.load('model.joblib')

st.title('Maternal Health Risk Prediction')

st.sidebar.header('Input Parameters')
def user_input_features():
    age = st.sidebar.number_input('Age', min_value=10, max_value=100, value=25)
    systolic_bp = st.sidebar.number_input('SystolicBP', min_value=50, max_value=200, value=120)
    diastolic_bp = st.sidebar.number_input('DiastolicBP', min_value=30, max_value=130, value=80)
    bs = st.sidebar.number_input('Blood Sugar', min_value=0.0, max_value=20.0, value=5.0)
    body_temp = st.sidebar.number_input('Body Temperature', min_value=35.0, max_value=115.0, value=37.0)

    data = {
        'Age': age,
        'SystolicBP': systolic_bp,
        'DiastolicBP': diastolic_bp,
        'BS': bs,
        'BodyTemp': body_temp,

    }
    features = pd.DataFrame(data, index=[0])
    return features

df = user_input_features()

st.subheader('User Input Parameters')
st.write(df)

# Predict the risk level
prediction = model.predict(df)[0]
risk_levels = {0: 'Low Risk', 1: 'Medium Risk', 2: 'High Risk'}

st.subheader('Prediction')
st.write(f'Predicted Risk Level: {prediction}')
