import streamlit as st

import langchain_helper

st.title("Resturant Name Generator")

cuisine = st.sidebar.selectbox("Pick a Cuisine", ("Indian", "Italian", "Chinese", "Mexican", "Indian Veg", "South Indian", "Mughlai", "Thai", "Arabic", "Japanese", "Korean"))

if cuisine:
    response = langchain_helper.generate_resturant_name_and_items(cuisine)

    st.header(response['resturant_name'].strip())
    menu_items = response['menu_items'].strip().split(",")
    st.write("Menu Items")

    for item in menu_items:
        st.write("-", item)