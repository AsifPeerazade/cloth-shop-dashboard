import streamlit as st
import pandas as pd

st.title("🧵 Upload Cloth Shop Excel Files")

# Upload files (with different keys than session_state)
sales_file = st.file_uploader("Upload Sales Data", type=["xlsx"], key="sales_file")
purchase_file = st.file_uploader("Upload Purchase Data", type=["xlsx"], key="purchase_file")
expenses_file = st.file_uploader("Upload Expenses Data", type=["xlsx"], key="expenses_file")

# Submit button
if st.button("Submit"):
    if sales_file and purchase_file and expenses_file:
        # Store uploaded data in session_state with different keys
        st.session_state["sales_data"] = pd.read_excel(sales_file, engine="openpyxl")
        st.session_state["purchase_data"] = pd.read_excel(purchase_file, engine="openpyxl")
        st.session_state["expenses_data"] = pd.read_excel(expenses_file, engine="openpyxl")
        # Navigate to dashboard page
        st.switch_page("pages/1_Dashboard.py")
    else:
        st.warning("Please upload all three files before submitting.")
