import os
import streamlit as st
from dotenv import load_dotenv
from langchain.chat_models import ChatOpenAI
from langchain.schema import HumanMessage

# Load environment variables from .env file
load_dotenv()

# Set the OpenAI API key
openai_api_key = os.getenv("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")
huggingface_token = os.getenv("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")

if not openai_api_key:
    st.error("Please set the OPENAI_API_KEY environment variable in your .env file.")
if not huggingface_token:
    st.error("Please set the HUGGINGFACE_TOKEN environment variable in your .env file.")

# Function to load OpenAI model and get response
def get_openai_response(question):
    llm = ChatOpenAI(model_name="gpt-3.5-turbo", temperature=0.5, api_key=openai_api_key)
    message = HumanMessage(content=question)
    response = llm([message])
    return response.content

# Initialize our Streamlit app
st.set_page_config(page_title="Q&A Demo")
st.header("Siri's chatbot")

input_text = st.text_input("Input: ", key="input")
submit = st.button("Ask the question")

# If ask button is clicked
if submit and input_text:
    response_text = get_openai_response(input_text)
    st.subheader("The Response is")
    st.write(response_text)
