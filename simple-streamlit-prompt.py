
from dotenv import load_dotenv
import streamlit as st
from langchain.llms import OpenAI

load_dotenv()

llm = OpenAI(temperature=0.9)

text = st.text_area("Enter Text")
submit = st.button("Generate Response")


if submit:
    st.header("Response")
    with st.spinner(text = "Please Wait"):
        st.write(llm(text))