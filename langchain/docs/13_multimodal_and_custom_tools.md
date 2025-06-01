# 🛠️ Multi-modal and Custom Tools

LangChain supports more than just plain text. With **multi-modal models** and **custom tools**, you can build applications that understand and respond to **images, audio, structured data, or even interact with APIs and files**.

---

## 🎯 Why Use Multi-modal or Custom Tools?

- Extend LLMs with **external functionality**
- Let agents access your business logic or APIs
- Enable workflows with **images, files, or structured data**
- Add domain-specific capabilities to your chains

---

## 🖼️ Example: Using `gpt-4o` for Vision Tasks

```python
from langchain_openai import ChatOpenAI
from langchain_core.messages import HumanMessage
from langchain_core.messages.tool import ToolMessage
import base64

# You must have gpt-4o access
llm = ChatOpenAI(model="gpt-4o", api_key="your-api-key")

# Example message with image (binary)
with open("example.jpg", "rb") as img_file:
    image_bytes = base64.b64encode(img_file.read()).decode("utf-8")

response = llm.invoke([
    HumanMessage(content=[
        {"type": "image_url", "image_url": {"url": "data:image/jpeg;base64," + image_bytes}}
    ])
])

print(response.content)
```

> ⚠️ `gpt-4o` supports vision input, but ensure your API access tier includes it.

---

## 🛠️ Create a Custom Tool

You can define custom logic that an agent can call. Use the `@tool` decorator:

```python
from langchain.tools import tool

@tool
def calculate_area(length: float, width: float) -> float:
    """Calculates area of a rectangle."""
    return length * width
```

Then include it in your toolset:

```python
tools = [calculate_area]
```

Agents will now be able to call this when reasoning through tasks like:

> "What's the area of a rectangle that's 5m long and 2m wide?"

---

## 📄 Custom Tool for File Reading

```python
@tool
def read_file(file_path: str) -> str:
    """Reads text from a local file."""
    with open(file_path, "r") as f:
        return f.read()
```

You can combine this tool with agents to allow them to:

* Search local files
* Extract information dynamically
* Chain it into a retrieval or QA task

---

## 🧩 Custom Tools with External APIs

```python
@tool
def get_weather(city: str) -> str:
    """Fetches current weather for a city from OpenWeatherMap."""
    import requests
    import os
    api_key = os.getenv("OPENWEATHER_API_KEY")
    response = requests.get(f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}")
    return response.json()["weather"][0]["description"]
```

> 📝 Store your API keys in a `.env` file and use `dotenv` to load them securely.

---

## 🧠 Agents Can Use These Tools

Include your tools in an agent's toolset using:

```python
from langchain.agents import initialize_agent, AgentType

agent = initialize_agent(
    tools=tools,
    llm=llm,
    agent=AgentType.ZERO_SHOT_REACT_DESCRIPTION,
    verbose=True
)
```

---

## ✅ Summary

* LangChain supports **multi-modal input** with models like `gpt-4o`
* **Custom tools** allow LLMs to perform calculations, API calls, and file interactions
* Tools can be created using `@tool` and used by agents or chains
* Combine tools + agents for dynamic, intelligent workflows

---

## 🧭 What's Next?

In [14_langgraph.md](./14_langgraph.md), you'll explore **LangGraph**, an optional but powerful extension to model complex logic flows using a node-based, state-machine architecture.

