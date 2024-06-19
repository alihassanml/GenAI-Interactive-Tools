import google.generativeai as genai
import os
import streamlit as st
import PIL.Image


st.title('Gernative Ai Gemna Visison Pro')
os.environ['API_KEY'] = 'Your Api Key'

genai.configure(api_key=os.environ['API_KEY'])
model = genai.GenerativeModel('gemini-1.5-flash')


def VisionModel(input,image):
    if input!='':
        output = model.generate_content([input,image])
        
    else:
        output = model.generate_content(image)
        
    return output.text
      





user_input = st.text_input('Enter Input')
user_image = st.file_uploader('Chose Image',type=['jpeg','png','jpg','avif'])

if user_image:
    image = PIL.Image.open(user_image)
    st.image(image,caption='Uploaded Image',use_column_width=True)
   

submit = st.button('Tell Me About This Image')
if submit:
    image = PIL.Image.open(user_image)
    response =  VisionModel(user_input,image)
    st.header('Response')
    st.write(response)
