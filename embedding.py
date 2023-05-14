import os
from dotenv import load_dotenv

from langchain.embeddings import OpenAIEmbeddings
from langchain.embeddings.openai import OpenAIEmbeddings

load_dotenv()

embeddings = OpenAIEmbeddings()

text = "This is a test document."

query_result = embeddings.embed_query(text)

doc_result= embeddings.embed_documents([text])

print(query_result)
print(doc_result)