import os
from dotenv import load_dotenv
import streamlit as st
from langchain.llms import OpenAI
from langchain.agents import load_tools
from langchain.agents import initialize_agent
from langchain.agents import AgentType
from langchain.chat_models import ChatOpenAI
from langchain import ConversationChain

load_dotenv()

chat = ChatOpenAI(temperature=0)

llm = OpenAI(temperature=0)

tools = load_tools(["serpapi", "llm-math"], llm = llm)

agent = initialize_agent(tools, chat,
                         agent=AgentType.CHAT_ZERO_SHOT_REACT_DESCRIPTION, verbose = True)

text = st.text_area("Enter Text")
submit = st.button("Generate Response")

if submit:
    st.header("Response")
    with st.spinner(text = "Please Wait"):
        st.write(agent.run(text))