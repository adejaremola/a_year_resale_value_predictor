import pickle
import streamlit as st
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
price_in_thousands = st.slider("Price_in_thousands", min_value=3, max_value=53, value=26)
curb_weight = st.slider("Curb_weight", min_value=1.895, max_value=4.9825, value=2.0)

# When the 'Predict' button is clicked
if st.button("Predict"):
    # Make prediction using the input values
    input_data = [manufacturer, price_in_thousands, curb_weight]  # Collect the input features
    prediction = model.predict(np.array([input_data]))
    st.write(f'The predicted value is: {prediction}')
