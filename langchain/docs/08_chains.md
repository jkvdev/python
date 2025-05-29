# 🔗 Chains in LangChain

A **Chain** is a reusable sequence of components where the output of one becomes the input to the next. LangChain Chains let you go beyond single prompts by combining models, templates, memory, and even tools into structured workflows.

---

## 🎯 Why Use Chains?

- Orchestrate multi-step logic (e.g., search → summarize → respond)
- Reuse and test steps independently
- Combine LLMs with tools or memory
- Cleanly separate prompt logic from execution

---

## 🧱 Common Chain Types

| Chain Type              | Description                                    |
| ----------------------- | ---------------------------------------------- |
| `LLMChain`              | Prompt → LLM → Output                          |
| `SimpleSequentialChain` | Series of `LLMChain`s, passing outputs forward |
| `ConversationChain`     | Adds memory to track context                   |
| `SequentialChain`       | Multi-input/output logic across steps          |

---

## 🔹 1. Basic `LLMChain` Example

Here's how to create a basic LLM-powered chain with a custom prompt:

```python
from langchain_openai import ChatOpenAI
from langchain.chains import LLMChain
from langchain.prompts import PromptTemplate
from dotenv import load_dotenv
import os

load_dotenv()
api_key = os.getenv("OPENAI_API_KEY")

llm = ChatOpenAI(api_key=api_key)

prompt = PromptTemplate.from_template(
    "What is a good name for a company that makes {product}?"
)

chain = LLMChain(llm=llm, prompt=prompt)

response = chain.invoke({"product": "eco-friendly shoes"})
print(response['text'])
```

---

## 🔹 2. `SimpleSequentialChain`: Combine Chains

Useful when you want to pipe multiple `LLMChain`s in sequence:

```python
from langchain.chains import SimpleSequentialChain

chain1 = LLMChain(
    llm=llm,
    prompt=PromptTemplate.from_template("Translate this to French: {text}")
)

chain2 = LLMChain(
    llm=llm,
    prompt=PromptTemplate.from_template("Now make it more formal: {text}")
)

overall_chain = SimpleSequentialChain(chains=[chain1, chain2], verbose=True)

response = overall_chain.invoke("How are you?")
print(response)
```

---

## 🔹 3. `ConversationChain` with Memory

Great for building chatbots that remember what the user said:

```python
from langchain.memory import ConversationBufferMemory
from langchain.chains import ConversationChain

memory = ConversationBufferMemory()
chat = ConversationChain(llm=llm, memory=memory)

chat.invoke({"input": "My name is Carlos."})
response = chat.invoke({"input": "What's my name?"})
print(response['response'])  # Should recall "Carlos"
```

---

## 🔹 4. `SequentialChain`: Advanced Logic with Named Inputs/Outputs

Unlike `SimpleSequentialChain`, `SequentialChain` lets you define **explicit variable names** to pass outputs from one step to the next:

```python
from langchain.chains import SequentialChain

# First step: generate a company name
chain1 = LLMChain(
    llm=llm,
    prompt=PromptTemplate.from_template("Suggest a name for a company that makes {product}"),
    output_key="company_name"
)

# Second step: write a tagline using the company name
chain2 = LLMChain(
    llm=llm,
    prompt=PromptTemplate.from_template("Write a tagline for {company_name}"),
    output_key="tagline"
)

sequential_chain = SequentialChain(
    chains=[chain1, chain2],
    input_variables=["product"],
    output_variables=["company_name", "tagline"],
    verbose=True
)

response = sequential_chain.invoke({"product": "eco-friendly shoes"})
print(response)
```

> 🧩 Use `SequentialChain` when you need to pass variables between steps explicitly or manage multiple inputs/outputs in your logic.

---

## 🧭 Which Chain to Use?

| If you need...                | Use...                  |
| ----------------------------- | ----------------------- |
| Prompt → Model → Output       | `LLMChain`              |
| Sequence of LLMChains         | `SimpleSequentialChain` |
| Memory + Dialogue             | `ConversationChain`     |
| Complex variable dependencies | `SequentialChain`       |

---

## ✅ Summary

* **Chains** are composable units of logic built on top of LLMs
* Start with `LLMChain` for simple use cases
* Use `ConversationChain` to retain memory across steps
* Use `SimpleSequentialChain` for linear pipelines
* Use `SequentialChain` for complex workflows with multiple named inputs/outputs

---

## 🧭 What's Next?

In [09_retrievers.md](./09_retrievers.md), you'll learn how to integrate **vector-based retrieval** so your app can look up and use relevant documents before responding.
