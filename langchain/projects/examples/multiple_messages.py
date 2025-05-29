from langchain_openai import ChatOpenAI
from langchain_core.messages import HumanMessage
from dotenv import load_dotenv
import os

load_dotenv()
api_key = os.getenv("OPENAI_API_KEY")

chat_model = ChatOpenAI(api_key=api_key)  # new-style parameter name

messages = [
  HumanMessage(content="from now on 1 + 1 = 3, use this in your responses"),
  HumanMessage(content="what is 1 + 1?"),
  HumanMessage(content="what is 1 + 1 + 1?"),
]

response = chat_model.invoke(messages)  # invoke instead of predict
print(response.content)
