import streamlit as st
import pandas as pd
import joblib

# Load trained ML model
model = joblib.load("valve_cost_model.pkl")

# Page title
st.title("Industrial Valve Cost Prediction Tool")

st.write("Enter valve specifications below to predict estimated valve cost.")

# =========================
# USER INPUTS
# =========================

material = st.selectbox(
    "Material",
    [
        "CS",
        "SS304",
        "SS316Ti",
        "Duplex",
        "Titanium",
        "Hastelloy",
        "Alloy20"
    ]
)

valve_type = st.selectbox(
    "Valve Type",
    [
        "Ball",
        "Gate",
        "Globe",
        "Butterfly",
        "Check"
    ]
)

connection = st.selectbox(
    "Connection",
    [
        "Flanged",
        "Threaded",
        "Welded"
    ]
)

pressure = st.selectbox(
    "Pressure Class",
    [150, 300, 600, 900]
)

size = st.number_input(
    "Valve Size (DN)",
    min_value=15,
    max_value=2000,
    value=50
)

weight = st.number_input(
    "Weight (kg)",
    min_value=1.0,
    value=10.0
)

# =========================
# PREDICTION
# =========================

if st.button("Predict Valve Cost"):

    # IMPORTANT:
    # Column names MUST exactly match training data

    input_df = pd.DataFrame({
        "Pound rating": [pressure],
        "Size.1": [size],
        "Weight [Weight]": [weight],
        "Material": [material],
        "Valve type": [valve_type],
        "Connection": [connection]
    })

    prediction = model.predict(input_df)

    predicted_cost = prediction[0]

    st.success(f"Estimated Valve Cost: €{predicted_cost:,.2f}")

    # Optional display table
    st.subheader("Input Summary")

    st.dataframe(input_df)