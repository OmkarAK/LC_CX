# Static Prompting Approach : Not used generally
from langchain_huggingface import HuggingFaceEndpoint, ChatHuggingFace
from langchain.prompts import PromptTemplate
from dotenv import load_dotenv
import streamlit as st

load_dotenv()

llm = HuggingFaceEndpoint(
    repo_id="google/gemma-2b-it",
    task="text-generation"
)

model = ChatHuggingFace(llm=llm)

st.header("Research Tool")

user_input = st.text_input("Enter prompt")

if st.button("Summaize"):
    result = model.invoke(user_input)
    st.write(result.content)