
import streamlit as st
import joblib
import numpy as np



st.title("Salary Prediction app")

st.divider()


st.write("With This App, You Can Get Estimations For The Salaries Of The Company Employees ")

years = st.number_input("Enter the years at company ", value = 1, step = 1, min_value = 0)
jobrate = st.number_input("Enter the job Rate", value = 3.5, step = 0.5, min_value = 0.0)

x=(years,jobrate)

model = joblib.load("model/linearmodel.pkl")

st.divider()

predict = st.button("Press The Button For Salary Prediction")

st.divider()

if predict:

    st.balloons()

    x1 = np.array([x])

    prediction = model.predict(x1)

    st.write(f"Salary Prediction is {prediction}")


else:
    "please press the button for app to make the prediction"

