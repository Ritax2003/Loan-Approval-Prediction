import streamlit as st
import joblib
import pandas as pd

# Load the trained model
model = joblib.load('loan_approval_model.pkl')

# Define the function to make predictions
def predict_loan_approval(features):
    prediction = model.predict([features])
    return prediction[0]

# Streamlit app
st.title("Loan Approval Prediction System")

# Input fields for user data
st.sidebar.header("Enter Applicant Details")

# Example input fields
gender = st.sidebar.selectbox("Gender", options=[0, 1], format_func=lambda x: 'Male' if x == 1 else 'Female')
married = st.sidebar.selectbox("Married", options=[0, 1], format_func=lambda x: 'Yes' if x == 1 else 'No')
education = st.sidebar.selectbox("Education", options=[0, 1], format_func=lambda x: 'Graduate' if x == 1 else 'Not Graduate')
self_employed = st.sidebar.selectbox("Self Employed", options=[0, 1], format_func=lambda x: 'Yes' if x == 1 else 'No')
applicant_income = st.sidebar.number_input("Applicant Income", min_value=0, value=50000)
coapplicant_income = st.sidebar.number_input("Coapplicant Income", min_value=0.0, value=0.0)
loan_amount = st.sidebar.number_input("Loan Amount", min_value=0.0, value=10000.0)
loan_amount_term = st.sidebar.number_input("Loan Amount Term", min_value=0.0, value=360.0)
credit_history = st.sidebar.selectbox("Credit History", options=[0.0, 1.0], format_func=lambda x: 'No' if x == 0.0 else 'Yes')
property_area = st.sidebar.selectbox("Property Area", options=[0, 1, 2], format_func=lambda x: ['Urban', 'Semiurban', 'Rural'][x])
dependents = st.sidebar.number_input("Dependents", min_value=0, value=0)

# Collect inputs into a list
user_input = [gender, married, education, self_employed, applicant_income, coapplicant_income,
              loan_amount, loan_amount_term, credit_history, property_area, dependents]

# Predict
if st.sidebar.button("Predict"):
    result = predict_loan_approval(user_input)
    if result == 1:
        st.success("Loan Approved")
    else:
        st.error("Loan Denied")
