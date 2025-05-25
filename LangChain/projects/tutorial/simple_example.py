from langchain_openai import ChatOpenAI
from langchain_core.messages import HumanMessage
from dotenv import load_dotenv
import os

load_dotenv()
api_key = os.getenv("OPENAI_API_KEY")

chat_model = ChatOpenAI(api_key=api_key)  # new-style parameter name

response = chat_model.invoke([HumanMessage(content="hello")])  # invoke instead of predict
print(response.content)
