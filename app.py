import streamlit as st
import numpy as np
import pickle

# Load files
model = pickle.load(open("model.pkl", "rb"))
scaler = pickle.load(open("scaler.pkl", "rb"))

st.title("Customer Churn Prediction")

# Inputs
gender = st.selectbox("Gender", ["Male", "Female"])
SeniorCitizen = st.selectbox("Senior Citizen", [0, 1])
Partner = st.selectbox("Partner", ["Yes", "No"])
Dependents = st.selectbox("Dependents", ["Yes", "No"])
tenure = st.number_input("Tenure", 0, 100)
PhoneService = st.selectbox("Phone Service", ["Yes", "No"])
MultipleLines = st.selectbox("Multiple Lines", ["Yes", "No", "No phone service"])
Contract = st.selectbox("Contract", ["Month-to-month", "One year", "Two year"])
TotalCharges = st.number_input("Total Charges")

# Encoding (SAME as training)
gender = 1 if gender == "Male" else 0
Partner = 1 if Partner == "Yes" else 0
Dependents = 1 if Dependents == "Yes" else 0
PhoneService = 1 if PhoneService == "Yes" else 0

if MultipleLines == "Yes":
    MultipleLines = 1
elif MultipleLines == "No":
    MultipleLines = 0
else:
    MultipleLines = 2

if Contract == "Month-to-month":
    Contract = 1
elif Contract == "One year":
    Contract = 2
else:
    Contract = 3

# Input array
input_data = np.array([[gender, SeniorCitizen, Partner, Dependents,
                        tenure, PhoneService, MultipleLines,
                        Contract, TotalCharges]])

# Scale
input_data = scaler.transform(input_data)

# Predict
if st.button("Predict"):
    result = model.predict(input_data)

    if result[0] == 1:
        st.error("Customer will churn ❌")
    else:
        st.success("Customer will not churn ✅")
