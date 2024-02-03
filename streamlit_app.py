import streamlit as st
import pandas as pd

st.title("My Mom's Favourite Healthy Dinner")

st.header('Breakfast Favourite')
st.text('Hard Boiled Egg')
st.text('Avocado Toast')

my_fruit_list = pd.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")
my_fruit_list = my_fruit_list.set_index('Fruit')
st.title("Build Your Own Smoothie")
st.text("Filter Fruits By Name")
st.mutiselect('',list(my_fruit_list.index))
st.dataframe(my_fruit_list)
