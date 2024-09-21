
import streamlit as st
import joblib
import pandas as pd


st.title("Olympics Medal Prediction App")


model_filename = 'best_random_forest_model.joblib'
model = joblib.load(model_filename)


def predict_medals(gold, silver, bronze, noc_encoded, competition_encoded):
    features = pd.DataFrame({
        'Gold': [gold],
        'Silver': [silver],
        'Bronze': [bronze],
        'NOC_encoded': [noc_encoded],
        'Competitions_encoded': [competition_encoded]
    })
    
    
    prediction = model.predict(features)
    return prediction[0]


st.header("Input the details of the competition and country:")
gold = st.number_input("Gold medals", min_value=0, step=1)
silver = st.number_input("Silver medals", min_value=0, step=1)
bronze = st.number_input("Bronze medals", min_value=0, step=1)


noc_encoded = st.number_input("NOC encoded value", min_value=0, step=1)
competition_encoded = st.number_input("Competition encoded value", min_value=0, step=1)


if st.button("Predict Total Medals"):
    total_medals = predict_medals(gold, silver, bronze, noc_encoded, competition_encoded)
    st.write(f"Predicted total medals: **{total_medals}**")
