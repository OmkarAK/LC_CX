from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder
from langchain_core.messages import HumanMessage
from langchain_huggingface import HuggingFaceEndpoint, ChatHuggingFace
from dotenv import load_dotenv

load_dotenv()

llm = HuggingFaceEndpoint(
    repo_id="google/gemma-2b-it",
    task="text-generation"
)

model = ChatHuggingFace(llm=llm)

chat_template = ChatPromptTemplate([
    ('system','You are a helpful assistant'),
    MessagesPlaceholder(variable_name='chat_history'),
    ('human','{query}')
])

chat_history = []
with open('chat_history.txt') as f:
    chat_history.extend(f.readlines())

# print(chat_history)

prompt = chat_template.invoke({'chat_history':chat_history,'query':'Where is my refund'})
# print(prompt)

result = model.invoke(prompt)
print(result.content)