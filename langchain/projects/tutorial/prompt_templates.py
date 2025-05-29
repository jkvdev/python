from langchain_openai import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate
from dotenv import load_dotenv
import os

# Load the API key from .env
load_dotenv()
api_key = os.getenv("OPENAI_API_KEY")

# Initialize the chat model
chat_model = ChatOpenAI(api_key=api_key)

prompt_template = "You are a helpful assistant that translates {input_language} to {output_language}."
human_template = "Translate the following text: {text}"

# Define the prompt using ChatPromptTemplate
chat_prompt = ChatPromptTemplate.from_messages([
    ("system", prompt_template),
    ("human", human_template)
])

# Format the messages
messages = chat_prompt.format_messages(
    input_language="English",
    output_language="Spanish",
    text="Hello, how are you?"
)

# Use invoke (replaces predict)
response = chat_model.invoke(messages)

# Print the content of the response
print(response.content)
