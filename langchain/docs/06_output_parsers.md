# 🧹 Output Parsers in LangChain

Output parsers allow you to **clean, structure, or extract** specific parts of an LLM's response. This is especially helpful when working with multi-step answers, structured data, or when you need consistency for downstream use.

---

## 🎯 Why Use Output Parsers?

- Clean up messy LLM responses
- Enforce structured formats (e.g., JSON, list, numeric values)
- Simplify further processing of model output
- Improve reliability of chaining steps

---

## 📦 Built-in Output Parsers

| Parser                           | Description                             |
| -------------------------------- | --------------------------------------- |
| `StrOutputParser`                | Returns plain text output as a string   |
| `CommaSeparatedListOutputParser` | Parses text into a Python list          |
| `JsonOutputParser`               | Parses text into structured JSON        |
| `PydanticOutputParser`           | Uses Pydantic models for validation     |
| `StructuredOutputParser`         | Extracts from LLM with formatting hints |

---

## 🔤 Example: Using `StrOutputParser`

```python
from langchain_openai import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser

chat_prompt = ChatPromptTemplate.from_messages([
    ("system", "You are a helpful assistant."),
    ("human", "What are 3 tips for staying focused?")
])

chat_model = ChatOpenAI(api_key="your-api-key")
parser = StrOutputParser()

chain = chat_prompt | chat_model | parser
response = chain.invoke({})

print(response)
```

---

## 📋 Example: Custom Parser for Math Answers

```python
from langchain_core.output_parsers import BaseOutputParser

class AnswerOnlyParser(BaseOutputParser):
    # A basic custom parser that splits on a keyword
    # # You can expand it with regex or more robust logic if needed
    def parse(self, text: str) -> str:
        if "answer =" in text:
            return text.split("answer =")[-1].strip()
        return "Unable to parse"
```

Then pipe it in:

```python
chain = prompt | model | AnswerOnlyParser()
response = chain.invoke({"problem": "5x = 20"})
print(response)  # 4
```

---

## 🔄 Example: List Parser

```python
from langchain_core.output_parsers import CommaSeparatedListOutputParser

# This simulates the LLM returning a comma-separated string
parser = CommaSeparatedListOutputParser()
text = "read books, take breaks, use focus apps"
parsed = parser.parse(text)

print(parsed)  # ['read books', 'take breaks', 'use focus apps']
```

---

## 💡 Tip: Combine with LLM Format Instructions

Some parsers (like `StructuredOutputParser`) can generate **formatting instructions** that you insert directly into your prompt to guide the LLM.

```python
from langchain_core.output_parsers import StructuredOutputParser
from langchain_core.pydantic_v1 import BaseModel, Field

class WeatherInfo(BaseModel):
    city: str = Field(..., description="Name of the city")
    temperature: int = Field(..., description="Temperature in Celsius")

parser = StructuredOutputParser.from_output_type(WeatherInfo)

print(parser.get_format_instructions())
```

You can include that string in your prompt to teach the model how to format its response.

---

## ✅ Summary

- Output parsers convert messy LLM output into clean formats
- Use built-in ones (`StrOutputParser`, `CommaSeparatedListOutputParser`, etc.) or define your own
- Use `StructuredOutputParser` + Pydantic for validated schemas
- Great for building **reliable, production-grade chains**

---

## 🧭 What's Next?

Ready to build more structured workflows? In [07_memory.md](./07_memory.md), you'll learn how to **store and recall previous messages** using memory objects like `ConversationBufferMemory`.
