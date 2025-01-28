import langchain_helper as lch
import streamlit as st

st.title("kid name generator")

kid_type = st.sidebar.selectbox("what is the gender?", ("boy","girl"))

if kid_type == "boy":
    country_name = st.sidebar.text_area(label="What country is your boy?",max_chars=10)

if kid_type == "girl":
    country_name = st.sidebar.text_area(label="What country is your girl?",max_chars=10)


if country_name:
    response = lch.generate_kid_name(kid_type,country_name)
    st.text(response)
