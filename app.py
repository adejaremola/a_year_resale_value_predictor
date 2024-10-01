import pickle
import streamlit as st
import numpy as np
import pandas as pd

# Load your model file
with open('model.pkl', 'rb') as f:
    model = pickle.load(f)

st.title('One Year Resale Value Predictor App')

# Add input widgets for user inputs
manufacturer = st.selectbox(
    "Manufacturer", 
    ["Dodge", "Ford", "Mercedes-B", "Toyota", "Chevrolet", "Nissan", "Chrysler", "Mitsubishi", 
     "Volvo", "Oldsmobile", "Lexus", "Mercury", "Pontiac", "Volkswagen", "Saturn", "Cadillac", 
     "Honda", "Plymouth", "Acura", "Buick", "Audi", "Jeep", "Porsche", "Hyundai", "BMW", "Lincoln", 
     "Saab", "Subaru", "Jaguar", "Infiniti"]
)
price_in_thousands = st.slider("Price (thousand dollars)", min_value=3, max_value=53, value=26)
curb_weight = st.slider("Curb Weight", min_value=1, max_value=5, value=2)

# When the 'Predict' button is clicked
if st.button("Predict"):
    # Prepare the input data as a DataFrame (since pipelines often expect a DataFrame)
    input_data = pd.DataFrame({
        'Manufacturer': [manufacturer],
        'Price_in_thousands': [price_in_thousands],
        'Curb_weight': [curb_weight]
    })
    prediction = model.predict(input_data)
    st.write(f'The predicted value is: {prediction} thousand dollars')
