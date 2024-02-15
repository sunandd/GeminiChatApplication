from dotenv import load_dotenv
load_dotenv()

import streamlit as st 
import os
import google.generativeai as genai 


genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

#LOAD GEMINI PRO TO GET RESPONCE

model=genai.GenerativeModel("gemini-pro")
def get_gemini_responce(question):
    responce=model.generate_content(question)
    return responce.text


#initiate streamlit app

st.set_page_config(page_title="Q$A POWER BY GEMINI AI")
st.header("Gemini Chat Application")
input=st.text_input("Input: ", key="input")
submit=st.button("Submit the question")

# Handle response
if submit:
    response = get_gemini_responce(input)
    st.subheader("Here is the Response")
    st.write(response)
