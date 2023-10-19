import streamlit

streamlit.title("🥣 Breakfast Menu")
streamlit.header("🥗Omega3 and blueberry Oatmeal")
streamlit.text(" 🐔Kale,Spinach & Rocket Smoothie")
streamlit.text(" 🥑🍞Hard-Boiled Free-Range Egg")
streamlit.text(" 🍞Avacado Toast")
streamlit.header('🍌🥭 Build Your Own Fruit Smoothie 🥝🍇')

import pandas
my_fruit_list = pandas.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt") 
streamlit.multiselect("Pick some fruits:", list(my_fruit_list.index))
.dataframe(my_fruit_list)
