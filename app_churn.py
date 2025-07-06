# Gender --> 1==Female, 2==Male
# Churn --> 1==Yes, 2==No
#Scaler is imported as scaler.pkl
#Model is imported as model.pkl
#Oreder of X is --> 'Age', 'Gender', 'Tenure', 'MonthlyCharges'


import joblib
import numpy as np
import streamlit as st

scaler =joblib.load("scaler.pkl")
model= joblib.load("model.pkl")

st.title("Churn Prediction App")

st.divider()

st.write("Please enter the values and hit the Predict button for getting a prediction")

st.divider()


age_input = st.number_input("Enter Age", min_value= 15, max_value = 100, value= 30)

tenure = st.number_input("Enter Tenure value", min_value = 0, max_value= 130, value =10)

monthlycharges= st.number_input("Enter the Charges", min_value= 30, max_value=150)


gender  = st.selectbox("Enter the Gender",["Male","Female"])

if gender:
    gender_selected = 1 if gender=="Female" else 0

st.divider()

predictbutton= st.button("Predict")

st.divider()

if predictbutton:
    gender_selected = 1 if gender =="Female" else 0 

    X = [age_input, gender_selected, tenure, monthlycharges]
    X1= np.array(X)
    X_array = scaler.transform([X1])
    prediction = model.predict(X_array)[0]
    predicted = "Yes" if prediction ==1 else "No"

    st.balloons()


    st.write(f"Predicted:{predicted}")    

else:
    st.write("Please enter the values and press the predict button")
