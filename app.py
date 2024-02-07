# app.py 
# Q&A Chatbot 

# imports 
from langchain.llms import OpenAI
from dotenv import load_dotenv
load_dotenv() # load the environment variables from .env 
import streamlit as st
import os

################################## Function to load OpenAI model and get responses
def get_openai_response(question):

    # create llm model
    llm = OpenAI(openai_api_key=os.getenv("OPEN_API_KEY"),
                 model_name="gpt-3.5-turbo-instruct", # old deprecated: "text-davinci-003",
                 temperature=0.5,)

    # get response using the inputted question 
    response = llm(question) 

    return response

################################## Initialize streamlit app 
st.set_page_config(page_title="Q&A Demo")
st.header("Simple Q and A 💬")
st.caption("This question and answer application utilizes large language models (LLMs) from the Langchain library. This app is for fun, and not necessarily an accurate source of information.")
st.caption("⏳ After submitting, please allow for a few seconds for your answer to load.")
st.caption("🌐 Examples: \"What is the capital of Canada?\", \"How big is Earth?\", \"Do dolphins have self-awareness?\"") 

# create a variable for the input 
input = st.text_input("Ask a question: ", key="input")

# call OpenAI to get the response 
response = get_openai_response(input)

# create a submit button 
submit = st.button("Submit")

# if the button is clicked, submit will be true 
if submit:
    #st.subheader("The response is:")
    st.write(response) # out the response 