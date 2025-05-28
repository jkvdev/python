from langchain_openai import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import BaseOutputParser
from dotenv import load_dotenv
import os

# Load the API key from .env
load_dotenv()
api_key = os.getenv("OPENAI_API_KEY")

# Custom Output Parser
class AnswerOutputParser(BaseOutputParser):
    def parse(self, text: str) -> tuple:
        """Parses the output of an LLM and returns (steps, answer)"""
        try:
            steps, answer = text.strip().rsplit("answer =", 1)
            return steps.strip(), answer.strip()
        except ValueError:
            return text.strip(), "Could not parse answer"

# Initialize the model
chat_model = ChatOpenAI(api_key=api_key)

# Prompt setup
prompt_template = (
    "You are a helpful assistant that solves math problems and shows your work. "
    "Output each step then return the answer in the following format:\n"
    "answer = <your answer here>.\n"
    "Make sure to output the answer in all lowercase letters and to have exactly one space and one equal sign before the answer."
)
human_template = "{problem}"

chat_prompt = ChatPromptTemplate.from_messages([
    ("system", prompt_template),
    ("human", human_template)
])

# Format messages
messages = chat_prompt.format_messages(
    problem="2x^2 - 5x + 3 = 0"
)

# Call the model
response = chat_model.invoke(messages)

# Parse the result
steps, answer = AnswerOutputParser().parse(response.content)

# Output
print("🧮 Steps:\n", steps)
print("\n✅ Final Answer:", answer)
