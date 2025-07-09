from langchain_core.prompts import ChatPromptTemplate, PromptTemplate
from langchain_huggingface import HuggingFaceEndpoint, ChatHuggingFace
from dotenv import load_dotenv

load_dotenv()

llm = HuggingFaceEndpoint(
    repo_id="google/gemma-2b-it",
    task="text-generation"
)

model = ChatHuggingFace(llm=llm)

template1 = PromptTemplate(
    template="Write a detailed report on {topic}",
    input_variables=['topic']

)

template2 = PromptTemplate(
    template="Write a 5 line summary on the following. /n {text}",
    input_variables=['text']
)

prompt1 = template1.invoke({'topic':'Blackhole'})
result1 = model.invoke(prompt1)

prompt2 = template2.invoke({'text':result1.content})
result2 = model.invoke(prompt2)
print(result2.content)