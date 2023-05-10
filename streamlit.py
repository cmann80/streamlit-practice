import streamlit as st
import pandas as pd

input_text = None
if 'output' not in st.session_state:
    st.session_state['output'] = 0
    
if st.session_state['output'] <=2:
    st.markdown("""
                #LLM Practice""")
    input_text = st.text_input("practice", disabled=False, placeholder="Enter prompt")
    st.session_state['output'] = st.session_state['output'] +1
else:
        st.info('refresh')