import streamlit as st
import pandas as pd
import requests as rq
import snowflake.connector

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
if fruityvice_response.status_code == 200 :
  normalize_fruityvice_res_json_df = pd.json_normalize(fruityvice_response.json()).set_index('id')
  st.dataframe(normalize_fruityvice_res_json_df)
else :
  st.text('Please enter the valid fruit name or try different fruit name')

my_cnx = snowflake.connector.connect(**st.secrets["snowflake"])
my_cur = my_cnx.cursor()
my_cur.execute("SELECT * from PC_RIVERY_DB.PUBLIC.FRUIT_LOAD_LIST")
my_data_row = my_cur.fetchall()
fruit_load_df = pd.DataFrame(my_data_row)
fruit_load_df.rename(columns = {0: 'Fruit Name'},inplace = True)
st.header('Fruit Load Contains')
st.dataframe(fruit_load_df)

fruit_cus_want_to_add = st.text_input('Which Fruit you want to add ?','')
if fruit_cus_want_to_add != '' :
  check_already_there = "Select * from PC_RIVERY_DB.PUBLIC.FRUIT_LOAD_LIST where FRUIT_NAME = '"+fruit_cus_want_to_add.lower()+"'"
  my_cur.execute(check_already_there)
  check_already_there_data_row = my_cur.fetchall()
  if len(check_already_there_data_row) = 0 : 
    insert_query = "INSERT INTO PC_RIVERY_DB.PUBLIC.FRUIT_LOAD_LIST values('"+fruit_cus_want_to_add.lower()+"')"
    my_cur.execute(insert_query)
    st.text('Thanks For Adding '+ fruit_cus_want_to_add.lower()) 
    my_cnx.commit()
  else :
    st.text('Already there in load')
my_cnx.close()
  
