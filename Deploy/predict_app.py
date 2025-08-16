# predict_app.py
import streamlit as st
import pandas as pd
import joblib
from datetime import datetime

# Load trained model
model = joblib.load("../Notebooks/used_car_price_model.pkl")

st.set_page_config(page_title="Used Car Price Predictor", layout="centered")
st.title("Used Car Price Predictor")

# Define brands and models
cars = pd.read_csv("../Data/cleaned_data_updated.csv")
cars_uni = cars.drop_duplicates(subset=["brand", "model"])

brand_model_dict = cars_uni.groupby("brand")["model"].apply(list).to_dict()
fuel_list = cars["fuel_type"].drop_duplicates().to_list()

# Layout
col1, col2 = st.columns(2)

with col1:
    brand = st.selectbox("Brand", list(brand_model_dict.keys()))
    year = st.slider("Year", 1980, datetime.now().year, 2015)
    fuel_type = st.selectbox("Fuel Type", fuel_list)
    condition = st.selectbox("Condition", ["Reconditioned", "Used"])
    transmission = st.selectbox("Transmission", ["Manual", "Automatic"])

with col2:
    # Dynamic model selection based on brand
    models_for_brand = brand_model_dict[brand]
    model_name = st.selectbox("Model Name", models_for_brand)
    kilometers_run = st.number_input("Mileage (km)", 0, 500000, 50000)

age = datetime.now().year - year
km_per_year = kilometers_run / age
# Check if all fields are filled
if not all(
    [brand, model_name, year, kilometers_run, fuel_type, transmission, condition]
):
    st.warning("⚠️ Please fill in all fields to get a prediction.")
else:
    # Prepare input
    input_df = pd.DataFrame(
        [
            [
                brand,
                model_name,
                year,
                kilometers_run,
                fuel_type,
                transmission,
                condition,
                age,
                km_per_year,
            ]
        ],
        columns=[
            "brand",
            "model",
            "year",
            "kilometers_run",
            "fuel_type",
            "transmission",
            "condition",
            "age",
            "km_per_year",
        ],
    )

    # spinner while predicting
    with st.spinner("Calculating estimated price..."):
        predicted_price = model.predict(input_df)[0]

    # output
    st.markdown(f"### Estimated Price: **${predicted_price:,.2f}**")
