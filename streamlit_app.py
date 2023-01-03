import streamlit

streamlit.title('My Parents New Healthy Diner')

streamlit.header('Breakfast Favorites 🥗')

streamlit.text('Kale 🥬, Spinash & Smoothie')

streamlit.text('🥚Hard-bolied eggs')

streamlit.text('🥑Avacado Toast')

import pandas
my_fruit_list = pandas.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")
my_fruit_list = my_fruit_list.set_index('Fruit')

# Let's put a pick here so they can pick the fruit they want to include
streamlit.multiselect ("Pick some fruits:", list(my_fruit_list.index))

#display the table on the page

streamlit.dataframe(my_fruit_list)
