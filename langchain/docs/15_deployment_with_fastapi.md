# 🚀 Deployment with FastAPI

LangChain apps can be deployed as **web APIs** using [FastAPI](https://fastapi.tiangolo.com/). This lets you expose your chains, agents, or tools to the web—perfect for building real-world applications, SaaS backends, or internal tools.

---

## 🧱 Why FastAPI?

- Easy to use and async-friendly
- Great developer experience and docs
- Automatic docs via Swagger UI
- Integrates well with LangChain's async features

---

## 📦 Installation

```bash
pip install fastapi uvicorn
```

---

## 🧪 Example: Expose a Chain as an API

### 🔧 chain\_setup.py

```python
# chain_setup.py
from langchain_openai import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
import os
from dotenv import load_dotenv

load_dotenv()
api_key = os.getenv("OPENAI_API_KEY")

# Chain: simple English → French translator
chat_prompt = ChatPromptTemplate.from_messages([
    ("system", "You translate English to French."),
    ("human", "Translate this: {text}")
])

llm = ChatOpenAI(api_key=api_key)
parser = StrOutputParser()

chain = chat_prompt | llm | parser
```

---

### 🖥 main.py

```python
# main.py
from fastapi import FastAPI
from pydantic import BaseModel
from chain_setup import chain

app = FastAPI()

class TranslationRequest(BaseModel):
    text: str

@app.post("/translate")
def translate(request: TranslationRequest):
    response = chain.invoke({"text": request.text})
    return {"translation": response}
```

---

## ▶️ Running the API

```bash
uvicorn main:app --reload
```

Visit:

* `http://localhost:8000/docs` → Swagger UI
* `http://localhost:8000/translate` → POST endpoint

Example request body:

```json
{
  "text": "Good morning"
}
```

---

## 🧪 Async Example (Optional)

If your LangChain components are async-compatible, use:

```python
@app.post("/translate/async")
async def translate_async(request: TranslationRequest):
    response = await chain.ainvoke({"text": request.text})
    return {"translation": response}
```

---

## ✅ Summary

* Use FastAPI to wrap LangChain chains or agents
* Create REST APIs with `POST` endpoints
* Enable async behavior with `.ainvoke()`
* Ideal for frontend integration, SaaS tools, and deployment

---

## 🎉 Congratulations!

You've completed the **LangChain Documentation Series** 🎯

You now understand:

* Prompts, models, memory, chains, and tools
* How to build retrieval pipelines
* How to deploy your LLM logic into real-world applications

Keep going with your journey and remember that devs never stop learning! 

> 📌 **Bonus:** For a deep dive into embeddings and how vectorstores really work, check out [16_embeddings_and_vectorstores.md](./16_embeddings_and_vectorstores.md)
