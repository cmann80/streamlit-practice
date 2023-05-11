

from langchain.llms import OpenAI
from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain
from langchain.agents import load_tools
from langchain.agents import initialize_agent
from langchain.agents import AgentType
from langchain import ConversationChain


llm = OpenAI(temperature=0)

# tools = load_tools(["serpapi", "llm-math"], llm = llm)

# agent = initialize_agent(tools, llm,
#                          agent=AgentType.ZERO_SHOT_REACT_DESCRIPTION, verbose = True)

# agent.run("what was the high temprature in Seattle today? What is that number raised to the .023 power?")

conversation = ConversationChain(llm=llm, verbose=True)

output = conversation.predict(input = "Hi there!")
print(output)

output = conversation.predict(input="I'm doing well! Just having a conversation with an AI.")
print(output)