from langchain_core.prompts import PromptTemplate
from langchain_huggingface import HuggingFaceEndpoint, ChatHuggingFace

from langchain.output_parsers import StructuredOutputParser, ResponseSchema

from dotenv import load_dotenv

load_dotenv()

llm = HuggingFaceEndpoint(
    repo_id="google/gemma-2b-it",
    task="text-generation"
)

model = ChatHuggingFace(llm=llm)

schema = [
    ResponseSchema(name='fact_1', description='Fact 1 for the topic'),
    ResponseSchema(name='fact_2', description='Fact 2 for the topic'),
    ResponseSchema(name='fact_3', description='Fact 3 for the topic')
]

parser = StructuredOutputParser.from_response_schemas(schema)


template = PromptTemplate(
    template= 'Give me 3 facts about {topic} \n {format_instruction}',
    input_variables=['topic'],
    partial_variables={'format_instruction':parser.get_format_instructions()}
)

chain = template | model | parser
result = chain.invoke({'topic':'Cricket'})
print(result)