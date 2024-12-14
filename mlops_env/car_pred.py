import streamlit as st
import pandas as pd
import pickle

# Load the model from disk using the correct path
model_path = "C:/Users/Babji/Documents/car_pred_model"
try:
    with open(model_path, 'rb') as f:
        model = pickle.load(f)
except FileNotFoundError:
    st.error(f"Model file not found at {model_path}. Please make sure the model is in the correct location.")
    model = None

# Load the CSV data using the correct path
csv_file_path = "C:/Users/Babji/Documents/cars24-car-price.csv"
try:
    cars_df = pd.read_csv(csv_file_path)
except FileNotFoundError:
    st.error(f"CSV file not found at {csv_file_path}. Please make sure the CSV file is in the correct location.")
    cars_df = None

# Check if the model and CSV are loaded properly, if not, stop the app
if model is None or cars_df is None:
    st.stop()  # Stop execution if files are missing

# Display title
st.title("Car Resale Price Prediction")

# Display the first few rows of the dataset
st.dataframe(cars_df.head())

# Define the input form for prediction
col1, col2 = st.columns(2)

fuel_type = col1.selectbox("Select the fuel type", ["Diesel", "Petrol", "CNG", "LPG", "Electric"])
engine = col1.slider("Set the Engine Power", 500, 5000, step=100)
transmission_type = col2.selectbox("Select the transmission type", ["Manual", "Automatic"])
seats = col2.selectbox("Enter the number of seats", [4, 5, 7, 9, 11])

# Encoding Categorical features
encode_dict = {
    "fuel_type": {'Diesel': 1, 'Petrol': 2, 'CNG': 3, 'LPG': 4, 'Electric': 5},
    "transmission_type": {'Manual': 1, 'Automatic': 2}
}

# Make prediction when the button is clicked
if st.button("Get Price"):
    try:
        # Encoding the categorical features
        encoded_fuel_type = encode_dict['fuel_type'][fuel_type]
        encoded_transmission_type = encode_dict['transmission_type'][transmission_type]
        
        # Prepare input data for prediction
        input_data = [2012.0, 2, 120000, encoded_fuel_type, encoded_transmission_type, 19.7, engine, 46.3, seats]
        
        # Predict the price using the model
        pred = model.predict([input_data])[0]
        
        # Display the predicted price
        st.header(f"Predicted Price: ₹{round(pred, 2)}")
    except Exception as e:
        st.error(f"An error occurred while making predictions: {e}")
