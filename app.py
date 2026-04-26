import streamlit as st
import pandas as pd
import pickle

# load model and scaler


model = pickle.load(open(r'D:\House_Price\lr_model (1).pkl','rb'))
scaler = pickle.load(open(r'D:\House_Price\scaler.pkl','rb'))

# title
st.title("🏠 House Price Prediction App")
st.write("Enter house details to predict price")

# input fields
square_footage = st.number_input('Square Footage', 500, 10000, 1500)
bedrooms = st.number_input('Number of Bedrooms', 1, 10, 3)
bathrooms = st.number_input('Number of Bathrooms', 1, 10, 2)
year_built = st.number_input('Year Built', 1900, 2025, 2010)
lot_size = st.number_input('Lot Size', 500.0, 10000.0, 2000.0)
garage_size = st.number_input('Garage Size', 0, 5, 1)
neighborhood = st.number_input('Neighborhood Quality (1-10)', 1, 10, 5)

# dataframe
input_data = pd.DataFrame({
    'Square_Footage':[square_footage],
    'Num_Bedrooms':[bedrooms],
    'Num_Bathrooms':[bathrooms],
    'Year_Built':[year_built],
    'Lot_Size':[lot_size],
    'Garage_Size':[garage_size],
    'Neighborhood_Quality':[neighborhood]
})

# scaling
input_scaled = scaler.transform(input_data)

# prediction
if st.button("Predict Price"):
    prediction = model.predict(input_scaled)[0]
    st.success(f"🏡 Estimated House Price: ₹ {prediction:,.2f}")