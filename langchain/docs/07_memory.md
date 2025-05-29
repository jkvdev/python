# 🧠 Memory in LangChain

Memory allows LangChain agents or chains to **retain information** from earlier parts of a conversation or session. This is essential for building multi-turn applications like chatbots, personal assistants, or long-running tasks.

---

## 🎯 Why Use Memory?

- Maintain context across interactions
- Build realistic chatbots or assistants
- Avoid passing the full history manually each time

---

## 📦 Available Memory Classes

| Memory Class                   | Description                                     |
|--------------------------------|-------------------------------------------------|
| `ConversationBufferMemory`     | Stores entire chat history in RAM              |
| `ConversationSummaryMemory`    | Stores a *summary* of prior messages           |
| `ConversationBufferWindowMemory` | Stores only the *last N* interactions         |
| `VectorStoreRetrieverMemory`   | Embedding-based memory with vector search      |

The default and most common choice is `ConversationBufferMemory`.

---

## 🧪 Basic Example with `ConversationBufferMemory`

```python
from langchain_openai import ChatOpenAI
from langchain.chains import ConversationChain
from langchain.memory import ConversationBufferMemory
from dotenv import load_dotenv
import os

# Load API key
load_dotenv()
api_key = os.getenv("OPENAI_API_KEY")

# Create model and memory
llm = ChatOpenAI(api_key=api_key)
memory = ConversationBufferMemory()

# Create conversation chain
conversation = ConversationChain(
    llm=llm,
    memory=memory,
    verbose=True
)

# Interact
response1 = conversation.invoke({"input": "My name is Diego."})
response2 = conversation.invoke({"input": "What's my name?"})

print(response2['response'])  # "Your name is Diego."
```

---

## 🔍 How It Works

Each time you call `.invoke()`, LangChain:

* Sends previous messages from memory to the prompt
* Appends the new interaction
* Updates the memory automatically

You don't need to manually track the history.

---

## 🧹 When to Use Other Memory Types

| Type                             | Use Case                                       |
| -------------------------------- | ---------------------------------------------- |
| `ConversationBufferWindowMemory` | Keep only the last N exchanges (saves tokens)  |
| `ConversationSummaryMemory`      | Summarize long chats to stay under token limit |
| `VectorStoreRetrieverMemory`     | Recall long-past data by semantic meaning      |

---

## ⚠️ Caution with Memory

* Memory is **per-chain**, not global
* If using LCEL (`|` pipelines), memory must be manually injected
* Memory adds **tokens** to each request → higher cost

---

## ✅ Summary

* Use memory for multi-turn conversations
* `ConversationBufferMemory` is the default choice
* Integrates automatically with `ConversationChain`
* Use summary or retriever memory for longer contexts

---

## 🧭 What's Next?

Coming up in [08_chains.md](./08_chains.md), you'll learn about **LangChain Chains**—the powerful pattern for linking multiple LLM calls, tools, and logic together.

