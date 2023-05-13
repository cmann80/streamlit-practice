
import os
from dotenv import load_dotenv
from langchain.llms import OpenAI
from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain

load_dotenv()

llm = OpenAI(temperature=0.9)

text = "What happened yesterday?"
print(llm(text))



prompt = PromptTemplate(
    input_variables=["product"],
    template="What is a good name for a company that makes {product}?"
)
print(prompt.format(product="colorful socks"))

chain = LLMChain(llm=llm, prompt=prompt)

print(chain.run("colorful socks"))