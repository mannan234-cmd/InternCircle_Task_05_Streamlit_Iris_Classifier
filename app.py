
import streamlit as st
import joblib
import numpy as np

# Load the trained model
model = joblib.load("iris_model.pkl")

# Page configuration
st.set_page_config(
    page_title="Iris Flower Classifier",
    page_icon="🌸",
    layout="centered"
)

# Application title
st.title("🌸 Iris Flower Classifier")

st.write(
    "Enter the flower measurements below and the trained "
    "Machine Learning model will predict the Iris species."
)

st.divider()

# Input section
st.subheader("Enter Flower Measurements")

sepal_length = st.slider(
    "Sepal Length (cm)",
    min_value=4.0,
    max_value=8.0,
    value=5.1,
    step=0.1
)

sepal_width = st.slider(
    "Sepal Width (cm)",
    min_value=2.0,
    max_value=4.5,
    value=3.5,
    step=0.1
)

petal_length = st.slider(
    "Petal Length (cm)",
    min_value=1.0,
    max_value=7.0,
    value=1.4,
    step=0.1
)

petal_width = st.slider(
    "Petal Width (cm)",
    min_value=0.1,
    max_value=2.5,
    value=0.2,
    step=0.1
)

st.divider()

# Prediction button
if st.button("🔍 Predict Flower Species"):

    # Prepare input data
    input_data = np.array([[
        sepal_length,
        sepal_width,
        petal_length,
        petal_width
    ]])

    # Make prediction
    prediction = model.predict(input_data)

    # Get prediction probabilities
    probabilities = model.predict_proba(input_data)

    # Map prediction to flower name
    class_names = [
        "Setosa",
        "Versicolor",
        "Virginica"
    ]

    predicted_species = class_names[prediction[0]]

    confidence = probabilities[0][prediction[0]] * 100

    # Display prediction
    st.success(f"Predicted Flower: {predicted_species} 🌸")

    st.metric(
        label="Prediction Confidence",
        value=f"{confidence:.2f}%"
    )

    # Display input values
    st.subheader("Input Values")

    st.write({
        "Sepal Length": sepal_length,
        "Sepal Width": sepal_width,
        "Petal Length": petal_length,
        "Petal Width": petal_width
    })
