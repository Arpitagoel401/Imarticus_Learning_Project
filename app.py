import streamlit as st
import pandas as pd
import joblib

# Load the trained model
model = joblib.load('heart_disease_model.pkl')

# Title and description
st.title("Heart Disease Prediction App")
st.write("This app predicts the likelihood of heart disease based on user input.")

# User input form
def user_input_features():
    # Collect user input based on the dataset columns
    gender = st.selectbox("Gender (0 = Female, 1 = Male)", options=[0, 1])
    age = st.number_input("Age", min_value=1, max_value=120, value=30)
    education = st.selectbox("Education (1 = High School, 2 = College, 3 = Graduate, etc.)", options=[1, 2, 3])
    current_smoker = st.selectbox("Current Smoker (0 = No, 1 = Yes)", options=[0, 1])
    cigs_per_day = st.number_input("Cigarettes Smoked Per Day", min_value=0, max_value=100, value=10)
    bpmeds = st.selectbox("Blood Pressure Medication (0 = No, 1 = Yes)", options=[0, 1])
    prevalent_stroke = st.selectbox("History of Stroke (0 = No, 1 = Yes)", options=[0, 1])
    prevalent_hyp = st.selectbox("History of Hypertension (0 = No, 1 = Yes)", options=[0, 1])
    diabetes = st.selectbox("Diabetes (0 = No, 1 = Yes)", options=[0, 1])
    tot_chol = st.number_input("Total Cholesterol (mg/dL)", min_value=100, max_value=400, value=200)
    sys_bp = st.number_input("Systolic Blood Pressure (mm Hg)", min_value=80, max_value=200, value=120)
    dia_bp = st.number_input("Diastolic Blood Pressure (mm Hg)", min_value=50, max_value=120, value=80)
    bmi = st.number_input("Body Mass Index (kg/m²)", min_value=10.0, max_value=50.0, value=25.0)
    heart_rate = st.number_input("Resting Heart Rate (beats per minute)", min_value=40, max_value=120, value=70)
    glucose = st.number_input("Glucose Level (mg/dL)", min_value=50, max_value=200, value=100)

    # Package the data into a DataFrame to match the feature names used by the model
    data = {
        'male': gender,
        'age': age,
        'education': education,
        'currentSmoker': current_smoker,
        'cigsPerDay': cigs_per_day,
        'BPMeds': bpmeds,
        'prevalentStroke': prevalent_stroke,
        'prevalentHyp': prevalent_hyp,
        'diabetes': diabetes,
        'totChol': tot_chol,
        'sysBP': sys_bp,
        'diaBP': dia_bp,
        'BMI': bmi,
        'heartRate': heart_rate,
        'glucose': glucose
    }

    features = pd.DataFrame(data, index=[0])

    # Drop the Age_Bins column if it exists
    if 'Age_Bins' in features.columns:
        features = features.drop(columns=['Age_Bins'])

    return features

input_df = user_input_features()

# Display user inputs
st.subheader("User Input Features")
st.write(input_df)

# Prediction
if st.button("Predict"):
    prediction = model.predict(input_df)
    if prediction[0] == 1:
        st.error("The model predicts that this individual is at risk of heart disease.")
    else:
        st.success("The model predicts that this individual is not at risk of heart disease.")
