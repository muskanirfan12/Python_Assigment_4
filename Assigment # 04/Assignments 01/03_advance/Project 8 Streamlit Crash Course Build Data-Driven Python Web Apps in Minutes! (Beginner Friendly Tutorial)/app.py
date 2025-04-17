import streamlit as st
import joblib
import os

st.title("Enter the feature value to get a prediction")

# Model load karne ki koshish karo
model_path = "Linear_regression_model.pkl"

if os.path.exists(model_path):
    model = joblib.load(model_path)

    feature_value = st.number_input("Enter a value:", min_value=0, max_value=10)

    if st.button("Predict"):
        prediction = float(model.predict([[feature_value]]))
        st.success(f"The predicted value is: {prediction:.2f}")

else:
    st.error(f"Model file '{model_path}' not found! Please make sure the file is in the correct directory.")
