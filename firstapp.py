import streamlit as st
st.write("Hello World")
name=st.text_input("Enter your name")
age=st.number_input("Enter your age")
st.write("Name:",name)
st.write("Age:",age)
st.code("import streamlit as st")