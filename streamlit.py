import streamlit as st

st.title("My first streamlit app")

name = st.text_input("Enter your Name")

if st.button("Say Hello"):
    if name:
        st.success(f"Hello {name}, Welcome to my page")
    else:
        st.warning("Please enter your Name")