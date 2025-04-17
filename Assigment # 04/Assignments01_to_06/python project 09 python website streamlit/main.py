import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# Page Configuration
st.set_page_config(page_title="Interactive Data Dashboard", layout="wide")

# Custom Styling
st.markdown(
    """
    <style>
        .main {
            background-color: #f4f4f4;
        }
        h1 {
            color: #ff6600;
            text-align: center;
        }
        .stButton>button {
            background-color: #ff6600;
            color: white;
            font-size: 16px;
        }
    </style>
    """,
    unsafe_allow_html=True
)

st.title("📊 Interactive Data Dashboard")

# Sidebar for file upload
st.sidebar.header("Upload CSV File")
uploaded_file = st.sidebar.file_uploader("Choose a CSV file", type="csv")

if uploaded_file is not None:
    df = pd.read_csv(uploaded_file)

    # Sidebar filters
    st.sidebar.header("Filter Data")
    columns = df.columns.tolist()
    selected_column = st.sidebar.selectbox("Select column to filter by", columns)
    unique_values = df[selected_column].unique()
    selected_value = st.sidebar.selectbox("Select value", unique_values)

    filtered_df = df[df[selected_column] == selected_value]
    st.sidebar.write(filtered_df)

    # Display Data
    st.subheader("📌 Data Preview")
    st.dataframe(df, height=250)
    
    st.subheader("📈 Data Summary")
    st.write(df.describe())
    
    # Plot Data
    st.subheader("📊 Data Visualization")
    x_column = st.selectbox("Select x-axis column", columns, key="x_column")
    y_column = st.selectbox("Select y-axis column", columns, key="y_column")
    
    if st.button("Generate Line Chart"):
        if x_column == y_column:
            st.warning("⚠️ Please select different columns for the x-axis and y-axis.")
        else:
            st.line_chart(filtered_df.set_index(x_column)[y_column])
else:
    st.warning("📂 Please upload a CSV file to get started!")