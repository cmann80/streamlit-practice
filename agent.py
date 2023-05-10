"""
My first app: practicing openAI input and output
"""

import streamlit as st
import pandas as pd
from langchain.llms import OpenAI
from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain
from langchain.agents import load_tools
from langchain.agents import initialize_agent
from langchain.agents import AgentType



llm = OpenAI(temperature=0)

tools = load_tools(["serpapi", "llm-math"], llm = llm)

agent = initialize_agent(tools, llm,
                         agent=AgentType.ZERO_SHOT_REACT_DESCRIPTION, verbose = True)

agent.run("what was the high temprature in Seattle today? What is that number raised to the .023 power?")

# llm = OpenAI(temperature=0.9)

# text = "What happened yesterday?"
# print(llm(text))

# prompt = PromptTemplate(
#     input_variables=["product"],
#     template="What is a good name for a company that makes {product}?"
# )
# print(prompt.format(product="colorful socks"))


# input_text = None
# if 'output' not in st.session_state:
#     st.session_state['output'] = 0
    
# if st.session_state['output'] <=2:
#     st.markdown("""
#                 #LLM Practice""")
#     input_text = st.text_input("practice", disabled=False, placeholder="Enter prompt")
#     st.session_state['output'] = st.session_state['output'] +1
# else:
#         st.info('refresh')