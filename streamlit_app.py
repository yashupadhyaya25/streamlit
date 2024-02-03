import streamlit as st
import pandas as pd

st.title("My Mom's Favourite Healthy Dinner")

st.header('Breakfast Favourite')
st.text('Hard Boiled Egg')
st.text('Avocado Toast')

my_fruit_list = pd.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")
my_fruit_list = my_fruit_list.set_index('Fruit')
st.title("Build Your Own Smoothie")
fruit_selected = st.multiselect('Choose Fruit',list(my_fruit_list.index))
if len(fruit_selected.values) > 0 :
  st.dataframe(my_fruit_list.loc[fruit_selected])
else :
  st.dataframe(my_fruit_list)
