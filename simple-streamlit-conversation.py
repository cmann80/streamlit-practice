
from dotenv import load_dotenv
import streamlit as st
from langchain.chat_models import ChatOpenAI
from langchain import PromptTemplate, LLMChain

from langchain.prompts.chat import (
    ChatPromptTemplate,
    SystemMessagePromptTemplate,
    AIMessagePromptTemplate,
    HumanMessagePromptTemplate,
)

from langchain.schema import (
    HumanMessage,
    SystemMessage
)

load_dotenv()

chat = ChatOpenAI(temperature = 0)

role = st.text_area("Enter the role you wish this AI to perform")

text = st.text_area("Enter Text")
submit = st.button("Generate Response")

template="You are a stern but caring {role}."
system_message_prompt = SystemMessagePromptTemplate.from_template(template)
example_human = HumanMessagePromptTemplate.from_template("Hi", additional_kwargs={"name": "example_user"})
example_ai = AIMessagePromptTemplate.from_template("I love you but I am stern.", additional_kwargs={"name": "example_assistant"})
human_template="{text}"
human_message_prompt = HumanMessagePromptTemplate.from_template(human_template)

chat_prompt = ChatPromptTemplate.from_messages([system_message_prompt, example_human, example_ai, human_message_prompt])
chain = LLMChain(llm=chat, prompt=chat_prompt)
# get a chat completion from the formatted messages


if submit:
    st.header("Response")
    with st.spinner(text = "Please Wait"):
        st.write(chain.run({"text": text, "role": role}))