import google.generativeai as genai
import os
import streamlit as st

st.title('Gernative Ai Using Gemna AI')
os.environ['API_KEY'] = 'AIzaSyDiWUOC6feuoOpT0NTmShelkREMcjptMNw'

genai.configure(api_key=os.environ['API_KEY'])
model = genai.GenerativeModel('gemini-1.5-flash')

user_input = st.text_input('Enter Text Here')
submit = st.button('Ask Question Here')
if user_input:
    response = model.generate_content(user_input)
    st.header('Response')
    st.write(response.text)


