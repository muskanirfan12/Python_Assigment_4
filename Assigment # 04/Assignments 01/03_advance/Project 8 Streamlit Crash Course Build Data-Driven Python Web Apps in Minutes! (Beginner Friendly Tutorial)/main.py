import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px

data = {
    "Name": ["Alice", "Bob", "Charlie", "David"],
    "Age": [25, 30, 35, 40],
    "City": ["New York", "Los Angeles", "Chicago", "Houston"],
    "Score": [85, 90, 95, 80],
}

df = pd.DataFrame(data)

st.title("Simple dataframe  display: ")
st.table(df)

name = st.selectbox("Select name to filter:" , df["Name"].unique())
filtered_data = df[df["Name"] == name]
st.dataframe(filtered_data)


#style data frame
value_of_style = st.number_input("Enter a value to style the dataframe:", min_value=0, max_value=100, value=90)
styled_dataframe = df.style.applymap(lambda x:"background-color: yellow" if isinstance(x , int) and x > value_of_style else "background-color: black")

st.dataframe(styled_dataframe)
st.markdown("**This is a simple dataframe display with a filter option.**")


st.write("line chart")

data = pd.DataFrame(
    np.random.randn(100, 4),
    columns=["a", "b", "c", "d"]
)

st.line_chart(data)
st.bar_chart(data)


data = pd.DataFrame({
    "Fruit" : ["Apples", "Oranges", "Bananas", "Grapes"],
    "Amount" : [4, 1, 2, 5],})


fig = px.bar(data, x="Fruit" , y="Amount" , title = "Fruit Sales")
st.plotly_chart(fig)