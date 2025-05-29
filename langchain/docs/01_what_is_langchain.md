# 📘 What is LangChain?

LangChain is a framework for developing applications powered by **language models** (LLMs), such as GPT-4. It provides modular, composable components and patterns to create intelligent systems that:

- Use prompt templates and chat models
- Maintain memory of a conversation
- Reason through steps using tools
- Retrieve context from documents and vector databases
- Compose complex workflows using agents

## 🤔 Why Use LangChain?

LangChain makes it easier to:

- Structure and reuse prompts
- Chain together multiple interactions
- Integrate external data sources (APIs, files, databases)
- Equip LLMs with tools like search or calculator
- Create real apps with memory and logic

---

## 🧠 Key Concepts Overview

| Concept            | Description                           |
| ------------------ | ------------------------------------- |
| **PromptTemplate** | Reusable prompts with placeholders    |
| **ChatModel**      | Interface to LLMs like GPT, Claude    |
| **Memory**         | Stores history of conversation        |
| **Chains**         | Sequences of prompt → model → parse   |
| **Agents**         | LLMs that choose and use tools        |
| **Retrievers**     | Lookup relevant chunks from documents |
| **Output Parsers** | Structure or format the model output  |

---

## 🔧 Simple Example: Using `ChatOpenAI` with a Prompt

```python
from langchain_openai import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate

chat_model = ChatOpenAI(api_key="your-api-key")

chat_prompt = ChatPromptTemplate.from_messages([
    ("system", "You are a helpful assistant that translates English to Spanish."),
    ("human", "Translate: {text}")
])

messages = chat_prompt.format_messages(text="Hello!")
response = chat_model.invoke(messages)

print(response.content)  # Hola!
```

---

## 🧱 LangChain Philosophy

LangChain promotes the **composition of logic** via chains and tools. Unlike traditional API calls to an LLM, LangChain encourages:

- Reusability (via chains)
- Reliability (via output parsers)
- Extensibility (via agents/tools)
- Maintainability (via templates and structure)

---

## 🚀 What’s Next?

👉 Continue to [02_installation_and_setup.md](./02_installation_and_setup.md) for setting up your environment and tools.
