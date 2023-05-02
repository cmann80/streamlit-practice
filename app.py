# import the modules
from PyPDF2 import PdfReader
import streamlit as st
import pandas as pd
from langchain.embeddings.openai import OpenAIEmbeddings
from langchain.text_splitter import CharacterTextSplitter
from langchain.vectorstores import ElasticVectorSearch, Pinecone, Weaviate, FAISS
from langchain.chains.question_answering import load_qa_chain
from langchain.llms import OpenAI
import os
import pickle
# load .env file
from dotenv import load_dotenv
load_dotenv()

#intake PDF
reader = PdfReader('epson-manual.pdf')

#read in raw text from reader
raw_text = ''
for i, page in enumerate(reader.pages):
    text = page.extract_text()
    if text:
        raw_text += text

#split text into words
text_splitter = CharacterTextSplitter(        
    separator = "\n",
    chunk_size = 1000,
    chunk_overlap  = 200,
    length_function = len,
)
texts = text_splitter.split_text(raw_text)

#activate open AI imbeddings
embeddings = OpenAIEmbeddings()
with open("foo.pkl", 'wb') as f:
    pickle.dump(embeddings, f)
    
    
with open("foo.pkl", 'rb') as f: 
    new_docsearch = pickle.load(f)
    
    
# Below method will list the most similar chunks that might contain the answer to the query
docsearch = FAISS.from_texts(texts, new_docsearch)




# streamlit

input_text = None
if 'output' not in st.session_state:
    st.session_state['output'] = 0
    
if st.session_state['output'] <=2:
    st.markdown("""
                LLM Practice""")
    input_text = st.text_input("practice", disabled=False, placeholder="Enter prompt")
    st.session_state['output'] = st.session_state['output'] +1
else:
        st.info('refresh')
        
        
        
#query input
query = input_text
docs = docsearch.similarity_search(query)
print(docs[0].page_content)


chain = load_qa_chain(OpenAI(temperature=0), chain_type="stuff")
chain.run(input_documents=docs, question=query)
