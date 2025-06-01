# 🧠 LangChain Documentation Series

Welcome to the **LangChain Docs** - a practical, beginner-friendly guide for building LLM-powered applications in Python using the [LangChain](https://www.langchain.com/) framework.

This documentation helps you progress from **zero to deployment**, even if you're new to advanced Python or LLMs. Each section includes clean code examples, clear explanations, and follows a logical learning path.

---

## 📘 Table of Contents

#### [01 - What is LangChain?](./01_what_is_langchain.md)

- A high-level overview of what LangChain is and why it's useful

#### [02 - Installation & Setup](./02_installation_and_setup.md)

- Setting up LangChain, installing dependencies, and configuring your API keys

#### [03 - LLMs and Chat Models](./03_llms_and_chat_models.md)

- How to use `ChatOpenAI`, message formats, model configuration, and `.invoke()`

#### [04 - Prompt Templates](./04_prompt_templates.md)

- Creating safe, reusable prompts using `PromptTemplate` and `ChatPromptTemplate`

#### [05 - LangChain Expression Language](./05_langchain_expression_language.md)

- Building modular pipelines using the `|` (pipe) syntax with prompts, models, and parsers

#### [06 - Output Parsers](./06_output_parsers.md)

- Cleaning and structuring raw model outputs using built-in and custom parsers

#### [07 - Memory](./07_memory.md)

- Maintaining conversation history with memory classes like `ConversationBufferMemory`

#### [08 - Chains](./08_chains.md)

- Creating logical pipelines using `LLMChain`, `SimpleSequentialChain`, and more

#### [09 - Retrievers](./09_retrievers.md)

- Retrieving document chunks based on user queries using vector similarity

#### [10 - Document Loaders](./10_document_loaders.md)

- Loading and chunking real-world documents from PDF, text, web, and directories

#### [11 - Tools and Agents](./11_tools_and_agents.md)

- Giving LLMs external abilities using tools and decision-making via agents

#### [12 - RetrievalQA](./12_retrieval_qa.md)

- Combining retrievers and LLMs to answer questions over your own data (RAG)

#### [13 - Multimodal & Custom Tools](./13_multimodal_and_custom_tools.md)

- Handling vision input (e.g., GPT-4o) and creating custom agent tools

#### [14 - LangGraph](./14_langgraph.md)

- Building complex, stateful workflows using LangChain's graph-based system

#### [15 - Deployment with FastAPI](./15_deployment_with_fastapi.md)

- Turning your chains or agents into real-time APIs using FastAPI and `uvicorn`

#### [16 - Embeddings and Vectorstores](./16_embeddings_and_vectorstores.md)
- How to convert text into vectors and use vectorstores like Chroma for retrieval

---

## 🚀 How to Use This Folder

1. Start from the top and progress through the files
2. Each file is standalone and includes examples you can run
3. Copy, adapt, and reuse the code in your own projects

---

## 🧩 Prerequisites

- Basic Python knowledge (functions, classes, packages)
- Python 3.10+ installed
- API key from [OpenAI](https://platform.openai.com)

---

## 🗣️ Feedback or Suggestions?

Found a bug or want to contribute? Fork and PR welcome!

Happy learning and building! 💡

> 📌 New: Check out [16_embeddings_and_vectorstores.md](./16_embeddings_and_vectorstores.md) to explore how semantic search works under the hood!