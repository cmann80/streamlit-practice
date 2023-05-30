
from dotenv import load_dotenv
import streamlit as st
from langchain.llms import OpenAI

load_dotenv()

llm = OpenAI(temperature=0.9)

text = st.text_area("enter text")
submit = st.button("generate response")


if submit:
    st.header("response")
    with st.spinner(text = "please wait"):
        st.write(llm(text))