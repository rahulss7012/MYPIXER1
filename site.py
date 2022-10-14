import streamlit as st
st.set_page_config(page_title="main page",page_icon="📷")
st.title("main page")
st.sidebar.success("select a page above")
if "my_input" not in st.session_state:
    st.session_state["my_input"]=""
my_input=st.text_input("input a text here",st.session_state["my_input"])
submit=st.button("submit")
if submit:
    st.session_state["my_input"]=my_input
    st.write("you have entered",my_input)