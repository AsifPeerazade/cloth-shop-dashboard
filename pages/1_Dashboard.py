import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# ---- Page Config ----
st.set_page_config(page_title="Cloth Shop | Dashboard", layout="wide")

# ---- Title ----
st.markdown("""
    <h1 style='text-align: center; color: #4B0082;'>🧵 Cloth Shop Dashboard</h1>
    <hr style="border:1px solid #999">
""", unsafe_allow_html=True)

# ---- Check if Data Exists in Session State ----
if "sales_data" not in st.session_state or "purchase_data" not in st.session_state or "expenses_data" not in st.session_state:
    st.warning("⚠️ Please upload the files on the Home page before accessing the dashboard.")
    st.stop()

# ---- Load Data ----
sales = st.session_state["sales_data"]
purchase = st.session_state["purchase_data"]
expenses = st.session_state["expenses_data"]

# ---- Clean Data ----
sales = sales[(sales["Quantity"] > 0) & (sales["SellingPrice"] > 0)]
purchase = purchase[(purchase["Quantity"] > 0) & (purchase["CostPrice"] > 0)]
expenses = expenses[expenses["Amount"] > 0]

# ---- Calculations ----
sales["TotalSale"] = sales["Quantity"] * sales["SellingPrice"]
purchase["TotalCost"] = purchase["Quantity"] * purchase["CostPrice"]

total_sales = sales["TotalSale"].sum()
total_purchase = purchase["TotalCost"].sum()
total_expense = expenses["Amount"].sum()
gross_profit = total_sales - total_purchase
net_profit = gross_profit - total_expense

# ---- KPIs Section ----
st.markdown("<h3 style='color:#008080;'>📊 Key Performance Indicators</h3>", unsafe_allow_html=True)
kpi1, kpi2, kpi3 = st.columns(3)

kpi1.metric("💵 Total Sales", f"₹{total_sales:,.0f}")
kpi2.metric("📦 Total Purchase", f"₹{total_purchase:,.0f}")
kpi3.metric("💰 Net Profit", f"₹{net_profit:,.0f}")

st.markdown("<hr style='border:1px solid #ccc;'>", unsafe_allow_html=True)

# ---- Sales by Item Chart ----
st.markdown("<h4 style='color:#6A5ACD;'>📈 Sales by Item</h4>", unsafe_allow_html=True)
item_sales = sales.groupby("Item")["TotalSale"].sum().reset_index()

fig, ax = plt.subplots(figsize=(10, 5))
bars = ax.bar(item_sales["Item"], item_sales["TotalSale"], color="#4682B4")
ax.set_xlabel("Item", fontsize=12)
ax.set_ylabel("Total Sales (₹)", fontsize=12)
ax.set_title("Sales Distribution by Item", fontsize=14)
ax.tick_params(axis='x', rotation=45)
st.pyplot(fig)

# ---- Expandable Data Sections ----
with st.expander("📄 View Sales Data"):
    st.dataframe(sales.style.background_gradient(cmap='YlGn'))

with st.expander("📄 View Purchase Data"):
    st.dataframe(purchase.style.background_gradient(cmap='Oranges'))

with st.expander("📄 View Expenses Data"):
    st.dataframe(expenses.style.background_gradient(cmap='Reds'))

# ---- Footer ----
st.markdown("<hr>", unsafe_allow_html=True)
st.markdown("<div style='text-align: center; color: gray;'>Cloth Shop Dashboard | Made with ❤️</div>", unsafe_allow_html=True)
