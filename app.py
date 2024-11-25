from dotenv import load_dotenv
from langchain_google_genai import ChatGoogleGenerativeAI
import streamlit as st
import os
from langchain.prompts import PromptTemplate
from langchain.chains.llm import LLMChain
from prompt import *

# Load environment variables from the .env file
load_dotenv()

# Access the environment variables just like you would with os.environ
GOOGLE_API_KEY = os.getenv("GOOGLE_API_KEY")



# Response Format For my LLM Model
def cold_email_generation(recipient_name, recipient_email, recipient_company, recipient_job_title, recipient_job_description, industry, tone, product_service, key_benefits):
    # Define the LLM
    llm = ChatGoogleGenerativeAI(model="gemini-1.5-pro-002", temperature=1, api_key=GOOGLE_API_KEY)  

    # Define the prompt
    prompt = PromptTemplate(
            input_variables=["recipient_name", "recipient_email", "recipient_company", "recipient_job_title", "recipient_job_description", "industry", "tone", "product_service", "key_benefits"], 
            template=PROMPT,
        )
      
    llm_chain = LLMChain(llm=llm, prompt=prompt)

    # Generate Response
    response=llm_chain.run({"recipient_name":recipient_name, 
                            "recipient_email":recipient_email,
                            "recipient_company":recipient_company,
                            "recipient_job_title":recipient_job_title,
                            "recipient_job_description":recipient_job_description,
                            "industry":industry,
                            "tone":tone,
                            "product_service":product_service,
                            "key_benefits":key_benefits})
    return response

# Streamlit app
st.set_page_config(page_title="Cold Email Generator")
st.header("Cold Email Generator")

# Input text
recipient_name = st.text_input("Enter the recipient's name")
recipient_email = st.text_input("Enter the recipient's email")
recipient_company = st.text_input("Enter the recipient's company")
recipient_job_title = st.text_input("Enter the recipient's job title")
recipient_job_description = st.text_area("Enter the recipient's job description")

# Side bar for parameters
with st.sidebar:
    st.title("Parameters:")
    industry=st.selectbox("Select the industry",["Technology","Finance","Healthcare","Marketing","None"])
    tone=st.selectbox("Select the tone",["Friendly","Professional","Respectful","None"])
    product_service=st.text_input("Enter the product or service")
    key_benefits=st.text_area("Enter the key benefits")

# Create a button to generate the cold email
if st.button("Generate Cold Email"):
    # Generate the cold email using the parameters
    response = cold_email_generation(recipient_name, recipient_email, recipient_company, recipient_job_title, recipient_job_description, industry, tone, product_service, key_benefits)
    st.write(response)