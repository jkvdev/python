from langchain_openai import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import BaseOutputParser
from dotenv import load_dotenv
import os

# Load the API key from .env
load_dotenv()
api_key = os.getenv("OPENAI_API_KEY")

# Initialize the model
chat_model = ChatOpenAI(api_key=api_key)


# Custom Output Parser
class CommaSeparatedListOutputParser(BaseOutputParser):
    def parse(self, text: str) -> tuple:
            return text.strip().split(", ")


# Prompt setup
prompt_template = """You are a helpful assistant who generates comma separated lists. A user will pass in a category, and you should generate 6 items in that category in a comma separated list format. ONLY return a comma separated list of items, and nothing else."""
human_template = "{text}"

chat_prompt = ChatPromptTemplate.from_messages([
    ("system", prompt_template),
    ("human", human_template)
])

# Pipe/chain commands together
chain = chat_prompt | chat_model | CommaSeparatedListOutputParser()
result = chain.invoke({"text": "colors"})

print(result)
