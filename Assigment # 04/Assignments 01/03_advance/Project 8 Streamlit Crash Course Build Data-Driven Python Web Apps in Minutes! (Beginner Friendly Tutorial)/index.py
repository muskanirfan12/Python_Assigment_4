import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns


data = pd.DataFrame(
    np.random.randn(100, 3),
    columns=["A", "B", "C"]
)

plt.figure(figsize=(10 , 6))
sns.scatterplot(x= data["A"] , y=data["B"])
st.title("Scatter plot of A vs B")

st.pyplot(plt)


##################################

co1 , col2 , col3 =st.columns(3)

with col3:
    st.header("Column 1")
    st.write("This is the first column.")
    st.button("Button 1")

with col2:
    st.header("Column 2")
    st.write("This is the second column.")
    st.button("Button 2")    

with col3:
    st.header("Column 3")
    st.write("This is the third column.")
    st.button("Button 3") 

##################################

with st.expander("See more details"):
    st.write("There are some additional details that can be toggled.")
    st.line_chart([1,2,3,4,5])

##########
st.sidebar.title("NAvigation")

option =st.sidebar.selectbox("Choose a page",["Home","About","Contact"])

if option == "Home":
    st.write("Welcome to the Home page")
elif option == "About":
    st.write("This is the About page")
elif option == "Contact":
    st.write("This is the Contact page")


#########

st.set_page_config(page_title="Thread App" , layout="wide")

st.title("Thread App")
st.subheader("This is a simple thread app")
