# app.py
import streamlit as st
import joblib
import pandas as pd

# Title for the web app
st.title("Olympics Medal Prediction App")

# Load the saved model
model_filename = 'best_random_forest_model.joblib'
model = joblib.load(model_filename)

# Function to make predictions
def predict_medals(gold, silver, bronze, noc_encoded, competition_encoded):
    features = pd.DataFrame({
        'Gold': [gold],
        'Silver': [silver],
        'Bronze': [bronze],
        'NOC_encoded': [noc_encoded],
        'Competitions_encoded': [competition_encoded]
    })
    
    # Predict the total medals using the model
    prediction = model.predict(features)
    return prediction[0]

# User inputs for the model
st.header("Input the details of the competition and country:")
gold = st.number_input("Gold medals", min_value=0, step=1)
silver = st.number_input("Silver medals", min_value=0, step=1)
bronze = st.number_input("Bronze medals", min_value=0, step=1)

# For simplicity, you can use encoded values for the NOC and Competitions for now
noc_encoded = st.number_input("NOC encoded value", min_value=0, step=1)
competition_encoded = st.number_input("Competition encoded value", min_value=0, step=1)

# Button to trigger prediction
if st.button("Predict Total Medals"):
    total_medals = predict_medals(gold, silver, bronze, noc_encoded, competition_encoded)
    st.write(f"Predicted total medals: **{total_medals}**")
