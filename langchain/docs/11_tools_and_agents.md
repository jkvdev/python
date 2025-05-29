# 🛠️ Tools & Agents in LangChain

**Agents** allow language models to **decide what actions to take** using a set of provided **tools**. This lets LLMs go beyond static responses and dynamically interact with the world—e.g., searching the web, using a calculator, or querying a database.

---

## 🎯 Why Use Agents?

- Enable **multi-step reasoning**
- Let the LLM choose tools dynamically
- Support use cases like assistants, analysts, planners, bots
- Power up with plug-and-play tools (search, math, code, etc.)

---

## 🧠 How It Works

1. You define a set of tools (e.g., search, calculator, retrieval)
2. LangChain provides an **agent executor**
3. The LLM chooses which tool to call and with what input
4. The agent repeats until the task is complete

---

## 🔧 Example: Using Tools with an Agent

```python
from langchain_openai import ChatOpenAI
from langchain.agents import Tool, initialize_agent
from langchain.agents.agent_types import AgentType
from langchain.tools import DuckDuckGoSearchRun
from dotenv import load_dotenv
import os

load_dotenv()
api_key = os.getenv("OPENAI_API_KEY")

# Create tools
search = DuckDuckGoSearchRun()
tools = [
    Tool(
        name="Search",
        func=search.run,
        description="Useful for answering questions about current events or general knowledge."
    )
]

# Create model
llm = ChatOpenAI(api_key=api_key)

# Initialize agent
agent = initialize_agent(
    tools=tools,
    llm=llm,
    agent=AgentType.ZERO_SHOT_REACT_DESCRIPTION,
    verbose=True
)

# Invoke
response = agent.invoke("What is the capital of Morocco?")
print(response)  # Expected output: "Rabat"
```

> 📝 **\*Note:** The response format may vary slightly depending on the LangChain version.\*

---

## 🔍 What Are Tools?

Tools are just **functions wrapped with metadata** so that an LLM can choose to use them.

You can define custom tools too:

```python
def multiply(a: str, b: str) -> str:
    return str(int(a) * int(b))

tools = [
    Tool(
        name="Multiply",
        func=lambda x: multiply(*x.split()),
        description="Multiplies two integers, e.g. '4 5'"
    )
]
```

---

## 🤖 Common Agent Types

| AgentType                          | Behavior Description                     |
| ---------------------------------- | ---------------------------------------- |
| `ZERO_SHOT_REACT_DESCRIPTION`      | Uses tool descriptions to choose actions |
| `CONVERSATIONAL_REACT_DESCRIPTION` | Adds chat memory + tool use              |
| `OPENAI_FUNCTIONS`                 | Uses OpenAI's function-calling interface |

> 📌 `REACT` stands for **Reason + Act** — the agent reasons about the task, then takes action via a tool.

---

## 🛠️ Built-in Tools

LangChain provides many ready-to-use tools:

- Search: `DuckDuckGoSearchRun`, `SerpAPIWrapper`
- Math: `llm-math`
- Python REPL: execute code
- Wikipedia: lookup articles
- Filesystem: read/write files
- Custom: define your own

> 🔗 See [LangChain Tool Docs](https://docs.langchain.com/docs/components/tools/) for a full list.

---

## 🔒 Security Tip

Be cautious when giving agents access to powerful tools like:

- Web search
- File I/O
- Arbitrary code execution

Always sanitize inputs and outputs where possible.

---

## ✅ Summary

- **Agents** let LLMs use tools through reasoning
- Tools are callable functions with descriptions
- Use `initialize_agent()` to create an interactive agent
- Choose agent type based on task needs (`REACT`, `FUNCTIONS`, etc.)

---

## 🧭 What's Next?

In [12_retrieval_qa.md](./12_retrieval_qa.md), we'll combine your knowledge of retrievers and chains to create a full **Retrieval-Augmented Generation (RAG)** pipeline.
