
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
                "Product_Weight": product_weight,
                "Product_Sugar_Content": product_sugar_content,
                "Product_Allocated_Area": product_allocated_area,
                "Product_MRP": product_mrp,
                "Store_Size": store_size,
                "Store_Location_City_Type": store_location_city_type,
                "Store_Type": store_type,
                "Product_Id_char": product_id_char,
                "Store_Age_Years": store_age_years,
                "Product_Type_Category": product_type_category
            }
            
            headers = {'Content-Type': 'application/json'}
            response = requests.post(f"{backend_url}/v1/predict", data=json.dumps(payload), headers=headers)
            
            if response.status_code == 200:
                prediction = response.json().get("prediction")
                st.success(f"Predicted Sales: ${prediction:,.2f}")
            else:
                st.error(f"Error from backend: {response.status_code} - {response.text}")
        except requests.exceptions.ConnectionError:
            st.error("Could not connect to the backend API. Please ensure the backend is running and the URL is correct.")
        except Exception as e:
            st.error(f"An error occurred: {e}")

st.markdown("### Upload CSV for Batch Prediction")

uploaded_file = st.file_uploader("Choose a CSV file", type="csv")

if uploaded_file is not None:
    if st.button("Predict Sales (Batch)"):
        if not backend_url:
            st.error("Please enter the Backend API URL.")
        else:
            try:
                files = {'file': uploaded_file.getvalue()}
                batch_response = requests.post(f"{backend_url}/v1/predictbatch", files=files)
                
                if batch_response.status_code == 200:
                    predictions_data = batch_response.json().get("predictions")
                    if predictions_data:
                        predictions_df = pd.DataFrame(predictions_data, columns=["Predicted Sales"])
                        st.write("Batch Predictions:")
                        st.dataframe(predictions_df)
                    else:
                        st.warning("No predictions received for the batch.")
                else:
                    st.error(f"Error from backend for batch prediction: {batch_response.status_code} - {batch_response.text}")
            except requests.exceptions.ConnectionError:
                st.error("Could not connect to the backend API for batch prediction. Please ensure the backend is running and the URL is correct.")
            except Exception as e:
                st.error(f"An error occurred during batch prediction: {e}")
