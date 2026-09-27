
import streamlit as st
import requests
import json
import pandas as pd

# Streamlit App Title
st.title("SuperKart Sales Predictor")

st.markdown("### Enter Product and Store Details to Predict Sales")

# Input fields for online prediction
product_weight = st.number_input("Product Weight", min_value=0.0, value=12.66)
product_sugar_content = st.selectbox("Product Sugar Content", ['Low Sugar', 'Regular', 'No Sugar', 'Non-Consumable'])
product_allocated_area = st.number_input("Product Allocated Area", min_value=0.0, value=0.027)
product_mrp = st.number_input("Product MRP", min_value=0.0, value=117.08)
store_size = st.selectbox("Store Size", ['Medium', 'High', 'Small'])
store_location_city_type = st.selectbox("Store Location City Type", ['Tier 2', 'Tier 1', 'Tier 3'])
store_type = st.selectbox("Store Type", ['Supermarket Type2', 'Departmental Store', 'Supermarket Type1', 'Food Mart'])
product_id_char = st.selectbox("Product ID Character (e.g., FD, NC)", ['FD', 'NC', 'DR'])
store_age_years = st.number_input("Store Age (Years)", min_value=0, value=16)
product_type_category = st.selectbox("Product Type Category", ['Food', 'Drinks', 'Non-Consumables'])

# Backend API URL (this should be replaced with your actual Codespace backend URL)
# For local testing, you might use 'http://localhost:7860'
# In Codespaces, it will be the service name if using a Docker Compose setup, or a forwarded port URL
backend_url = st.text_input("Backend API URL (e.g., http://localhost:7860 or Codespace URL)", "http://localhost:7860")

if st.button("Predict Sales (Online)"):
    if not backend_url:
        st.error("Please enter the Backend API URL.")
    else:
        try:
            payload = {
                
