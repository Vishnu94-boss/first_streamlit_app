import streamlit

streamlit.title('My Parents New Healthy Diner')

streamlit.header('Breakfast Favorites 🥗')

streamlit.text('Kale 🥬, Spinash & Smoothie')

streamlit.text('🥚Hard-bolied eggs')

streamlit.text('🥑Avacado Toast')

import pandas

my_fruit_list = pandas.readcsv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")

streamlit.dataframe(my_fruit_list)
