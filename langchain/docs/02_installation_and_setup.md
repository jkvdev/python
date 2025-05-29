# ⚙️ LangChain Installation & Setup

Before using LangChain, you'll need to install the core packages and set up your environment for working with LLMs like OpenAI.

---

## 📦 Step 1: Install Required Packages

You'll need the core LangChain libraries and an LLM provider (e.g., OpenAI):

```bash
pip install langchain langchain-openai
```

### Optional, but recommended:

For working with vector stores and document loaders:

```bash
pip install chromadb tiktoken pypdf unstructured
```

Other optional integrations:

- `faiss-cpu` - For local vector DBs
- `python-dotenv` - To load API keys from `.env`
- `langchainhub` - Access community chains/templates

---

## 🔐 Step 2: Get and Store Your API Key

To use OpenAI with LangChain, you need an API key.

1. Create an account at [platform.openai.com](https://platform.openai.com)
2. Generate your API key
3. Store it in a `.env` file (recommended):

```
OPENAI_API_KEY=your-api-key-here
```

Then load it in your code using `python-dotenv`:

```python
from dotenv import load_dotenv
import os

load_dotenv()
api_key = os.getenv("OPENAI_API_KEY")
```

---

## 💡 Step 3: Your First Working Example

```python
from langchain_openai import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate
from dotenv import load_dotenv
import os

# Load API key from .env file
load_dotenv()
api_key = os.getenv("OPENAI_API_KEY")

# Initialize the model
chat_model = ChatOpenAI(api_key=api_key)

# Simple chat prompt
prompt = ChatPromptTemplate.from_messages([
    ("system", "You are a friendly assistant."),
    ("human", "What is the capital of Spain?")
])

# This sends the message to OpenAI and prints the response
messages = prompt.format_messages()
response = chat_model.invoke(messages)

print(response.content)  # Madrid
```

---

## 🧱 Project Structure Tip

As your LangChain projects grow, it's helpful to structure them like this:

```
langchain_project/
├── .env
├── main.py
├── prompts/
│   └── translate_prompt.txt
├── chains/
│   └── translate_chain.py
├── utils/
│   └── parsers.py
└── docs/
    └── 01_what_is_langchain.md
```

---

## ✅ Next Up

Now that your environment is ready, move on to learn how to use **LLMs and Chat Models** in [03_llms_and_chat_models.md](./03_llms_and_chat_models.md).
