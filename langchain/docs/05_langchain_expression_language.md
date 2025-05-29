# 🔗 LangChain Expression Language (LCEL)

The LangChain Expression Language (LCEL) is a **functional, chainable syntax** that lets you connect components like prompts, models, and parsers using the `|` (pipe) operator.

It's a declarative, readable way to build processing pipelines.

---

## 🎯 Why Use LCEL?

- Build **modular pipelines**
- Make code more **declarative and readable**
- Compose components like **Prompt → Model → OutputParser**
- Supports `.invoke()` and `.stream()` natively

---

## 🧱 Basic Structure

```text
input → PromptTemplate → LLM → OutputParser
```

In LCEL:

```python
chain = prompt | model | parser
result = chain.invoke({"your": "input"})
```

---

## 📦 Full Example: Translate English to Spanish

```python
from langchain_openai import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser

# Prompt
chat_prompt = ChatPromptTemplate.from_messages([
    ("system", "You are a helpful assistant that translates English to Spanish."),
    ("human", "Translate: {text}")
])

# Model and parser
chat_model = ChatOpenAI(api_key="your-api-key")
parser = StrOutputParser()

# Chain with LCEL
chain = chat_prompt | chat_model | parser

# Run it
response = chain.invoke({"text": "Hello!"})
print(response)  # Hola!
```

---

## 🧪 Intermediate Example: Math Answer Extractor

```python
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import BaseOutputParser
from langchain_openai import ChatOpenAI

# Custom output parser
class AnswerParser(BaseOutputParser):
    def parse(self, text: str) -> str:
        return text.split("answer =")[-1].strip()

# Prompt
chat_prompt = ChatPromptTemplate.from_messages([
    ("system", "Solve the math problem and give final answer as: answer = <result>"),
    ("human", "{problem}")
])

# Chain
chain = chat_prompt | ChatOpenAI(api_key="your-api-key") | AnswerParser()

# Invoke
response = chain.invoke({"problem": "2x^2 - 4x = 0"})
print(response)  # e.g., 0 or 2
```

---

## 🚀 Benefits of LCEL

| Feature          | Benefit                          |
| ---------------- | -------------------------------- |
| `\|` pipe syntax | Clean, modular pipelines         |
| `.invoke()`      | Run synchronously                |
| `.stream()`      | Stream token-by-token            |
| `.batch()`       | Process multiple inputs          |
| Composability    | Easy to swap or reuse components |

---

## ✅ Summary

- LCEL uses `|` to compose LangChain objects
- You can connect: `Prompt | Model | Parser`
- `.invoke()` triggers the whole pipeline
- Cleaner than managing each step manually

---

## ➕ Bonus Tip: Partial Application

You can partially apply variables to a prompt:

```python
partial_prompt = chat_prompt.partial(input_language="English", output_language="Spanish")
```

This lets you fix certain variables ahead of time, while still allowing others to be passed dynamically at runtime.

---

## 🧭 What's Next?

Next up, learn how to **structure and clean the model outputs** using [06_output_parsers.md](./06_output_parsers.md), where you'll use `StrOutputParser`, custom classes, and structured output parsing.
