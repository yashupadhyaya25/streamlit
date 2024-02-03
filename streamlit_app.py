import streamlit as st

st.title("My Mom's Favourite Healthy Dinner")

st.header('Breakfast Favourite')
st.text('Hard Boiled Egg')
st.text('Avocado Toast')

st.title("Build Your Own Smoothie")
my_fruit_list = pandas.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")
st.dataframe(my_fruit_list)
