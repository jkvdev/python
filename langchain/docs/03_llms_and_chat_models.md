# 💬 LLMs and Chat Models in LangChain

LangChain provides a clean interface to work with **LLMs (Language Models)** and **Chat Models** like GPT-3.5/4 through `ChatOpenAI`.

---

## 🧠 LLMs vs Chat Models

| Type        | Example        | Input Type     | Notes                              |
|-------------|----------------|----------------|-------------------------------------|
| LLM         | `OpenAI()`     | Text string    | One-shot completions               |
| Chat Model  | `ChatOpenAI()` | Message list   | Multi-turn conversations, roles    |

> 💡 Use `ChatOpenAI` when working with multi-turn messages or role-based prompts.

---

## 🔧 Using `ChatOpenAI`

### 🔹 Step-by-step example:

```python
from langchain_openai import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate
from dotenv import load_dotenv
import os

# Load API key
load_dotenv()
api_key = os.getenv("OPENAI_API_KEY")

# Initialize model
chat_model = ChatOpenAI(api_key=api_key)

# Create a prompt
prompt = ChatPromptTemplate.from_messages([
    ("system", "You are a wise AI assistant."),
    ("human", "Tell me a productivity tip.")
])

# Format messages and invoke the model
messages = prompt.format_messages()
response = chat_model.invoke(messages)

print(response.content)
```

---

## 🔁 Supported Parameters

When initializing `ChatOpenAI`, you can customize behavior:

```python
chat_model = ChatOpenAI(
    api_key=api_key,
    temperature=0.7,      # creativity
    model="gpt-4",        # model version
    max_tokens=500        # response length
)
```

### 🔹 Common models:

* `"gpt-3.5-turbo"`
* `"gpt-4"`
* `"gpt-4o"` *(multimodal, cheaper, faster)*

---

## 🧪 Testing with Simple Inputs

For quick testing, you can pass raw message lists directly:

```python
from langchain_core.messages import HumanMessage

response = chat_model.invoke([
    HumanMessage(content="Summarize the plot of Inception.")
])

print(response.content)
```

> This is useful for quick prototyping, but using `ChatPromptTemplate` is more maintainable for real apps.

---

## ✅ Summary

* Use `ChatOpenAI` to connect with OpenAI models
* Format prompts with `ChatPromptTemplate`
* Use `.invoke()` for modern LangChain interaction
* Set `temperature`, `model`, and `max_tokens` as needed

---

## 🚀 What's Next?

Next up, learn how to **reuse and format prompts** using [04_prompt_templates.md](./04_prompt_templates.md), including dynamic placeholders and prompt injection prevention.

