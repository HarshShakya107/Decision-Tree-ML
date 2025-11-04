import streamlit as st
import pandas as pd
import pickle
with open('credit_risk_model.pkl', 'rb') as file:
    model = pickle.load(file)

st.set_page_config(page_title="Credit Risk Predictor", page_icon="💰", layout="centered")

st.title("💳 Credit Risk Prediction App")
st.write("### Predict whether a loan applicant is a **Good or Bad Credit Risk** using Decision Tree ML model.")

st.markdown("---")

st.sidebar.header("🧍‍♂️ Applicant Information")

person_age = st.sidebar.number_input("Age", min_value=18, max_value=100, step=1)
person_income = st.sidebar.number_input("Annual Income ($)", min_value=0)
person_emp_length = st.sidebar.number_input("Employment Length (Years)", min_value=0, max_value=50, step=1)
loan_amnt = st.sidebar.number_input("Loan Amount ($)", min_value=0)
loan_int_rate = st.sidebar.number_input("Interest Rate (%)", min_value=0.0, step=0.1)
loan_percent_income = st.sidebar.number_input("Loan Percent of Income", min_value=0.0, step=0.01)
cb_person_cred_hist_length = st.sidebar.number_input("Credit History Length (Years)", min_value=0, max_value=50, step=1)

st.sidebar.markdown("---")

st.sidebar.header("🏠 Home Ownership")
home_options = ["OTHER", "OWN", "RENT"]
person_home_ownership = st.sidebar.selectbox("Home Ownership Type", home_options)

st.sidebar.header("🎯 Loan Intent")
loan_intent = st.sidebar.selectbox(
    "Loan Purpose",
    ["EDUCATION", "HOMEIMPROVEMENT", "MEDICAL", "PERSONAL", "VENTURE"]
)

st.sidebar.header("💠 Loan Grade")
loan_grade = st.sidebar.selectbox(
    "Loan Grade (A-G)",
    ["B", "C", "D", "E", "F", "G"]
)

cb_person_default_on_file_Y = st.sidebar.selectbox("Previous Default on File?", ["No", "Yes"])


input_data = {
    'person_age': person_age,
    'person_income': person_income,
    'person_emp_length': person_emp_length,
    'loan_amnt': loan_amnt,
    'loan_int_rate': loan_int_rate,
    'loan_percent_income': loan_percent_income,
    'cb_person_cred_hist_length': cb_person_cred_hist_length,
    'person_home_ownership_OTHER': 1 if person_home_ownership == "OTHER" else 0,
    'person_home_ownership_OWN': 1 if person_home_ownership == "OWN" else 0,
    'person_home_ownership_RENT': 1 if person_home_ownership == "RENT" else 0,
    'loan_intent_EDUCATION': 1 if loan_intent == "EDUCATION" else 0,
    'loan_intent_HOMEIMPROVEMENT': 1 if loan_intent == "HOMEIMPROVEMENT" else 0,
    'loan_intent_MEDICAL': 1 if loan_intent == "MEDICAL" else 0,
    'loan_intent_PERSONAL': 1 if loan_intent == "PERSONAL" else 0,
    'loan_intent_VENTURE': 1 if loan_intent == "VENTURE" else 0,
    'loan_grade_B': 1 if loan_grade == "B" else 0,
    'loan_grade_C': 1 if loan_grade == "C" else 0,
    'loan_grade_D': 1 if loan_grade == "D" else 0,
    'loan_grade_E': 1 if loan_grade == "E" else 0,
    'loan_grade_F': 1 if loan_grade == "F" else 0,
    'loan_grade_G': 1 if loan_grade == "G" else 0,
    'cb_person_default_on_file_Y': 1 if cb_person_default_on_file_Y == "Yes" else 0
}

input_df = pd.DataFrame([input_data])

if st.button("🔍 Predict Credit Risk"):
    prediction = model.predict(input_df)[0]
    
    if prediction == 1:
        st.success("✅ This applicant is **Low Risk (Good Loan)** 💚")
    else:
        st.error("⚠️ This applicant is **High Risk (Bad Loan)** 🔴")

    st.markdown("---")
    st.subheader("📊 Model Input Summary")
    st.dataframe(input_df)


