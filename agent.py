

import os
from dotenv import load_dotenv

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

# agent = initialize_agent(tools, llm,
#                          agent=AgentType.ZERO_SHOT_REACT_DESCRIPTION, verbose = True)

# agent.run("what was the high temprature in Seattle today? What is that number raised to the .023 power?")

# conversation = ConversationChain(llm=llm, verbose=True)

# output = conversation.predict(input = "Hi there!")
# print(output)

# output = conversation.predict(input="I'm doing well! Just having a conversation with an AI.")
# print(output)

agent = initialize_agent(tools, chat,
                         agent=AgentType.CHAT_ZERO_SHOT_REACT_DESCRIPTION, verbose = True)

print(agent.run("Who is Olivia Wilde's boyfriend? What is his current age raised to the 0.23 power?"))