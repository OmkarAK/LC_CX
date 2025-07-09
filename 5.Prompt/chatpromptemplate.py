from langchain_core.prompts import ChatPromptTemplate
from langchain_huggingface import HuggingFaceEndpoint, ChatHuggingFace
from dotenv import load_dotenv

load_dotenv()

llm = HuggingFaceEndpoint(
    repo_id="google/gemma-2b-it",
    task="text-generation"
)

model = ChatHuggingFace(llm=llm)

chat_template = ChatPromptTemplate([
    ('system','You are a helpful {domain} expert'),
    ('human','Explain in simple terms about {topic}')
])

prompt = chat_template.invoke({'domain':'cricket','topic':'Runs'})
result = model.invoke(prompt)
print(result.content)
