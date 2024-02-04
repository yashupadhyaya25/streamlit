import streamlit as st
import pandas as pd
import requests as rq

st.title("💪🥗 My Mom's Favourite Healthy Dinner 🥗💪")

st.header('🍳 Breakfast Favourite 🍳')
st.text('Hard Boiled Egg')
st.text('Avocado Toast')

my_fruit_list = pd.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")
my_fruit_list = my_fruit_list.set_index('Fruit')
st.title("🥤 Build Your Own Smoothie 🥤")
fruit_selected = st.multiselect('🍓🍉🍒🍑 Choose Fruit 🍓🍉🍒🍑',list(my_fruit_list.index))
if len(fruit_selected) > 0 :
  st.dataframe(my_fruit_list.loc[fruit_selected])
else :
  st.dataframe(my_fruit_list)

st.header("Fruityvice Fruit Advice!")
fruit_choice = st.text_input('What fruit would you like information about?','Kiwi')
st.write('The user entered ', fruit_choice)
fruityvice_response = rq.get("https://fruityvice.com/api/fruit/"+fruit_choice)
normalize_fruityvice_res_json_df = pd.json_normalize(fruityvice_response.json()).set_index('id')
st.dataframe(normalize_fruityvice_res_json_df)

