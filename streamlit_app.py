import streamlit as st
import pandas as pd

st.title("My Mom's Favourite Healthy Dinner")

st.header('Breakfast Favourite')
st.text('Hard Boiled Egg')
st.text('Avocado Toast')

st.title("Build Your Own Smoothie")
st.text("Filter Fruits By Name")
st.mutiselect(list(my_fruit_list.index))
my_fruit_list = pd.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")
st.dataframe(my_fruit_list)
