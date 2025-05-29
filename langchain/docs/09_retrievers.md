# 📚 Retrievers in LangChain

Retrievers let you **search and return relevant chunks of data** from a collection of documents. They're typically used in **RAG pipelines**, where the LLM gets helpful context before generating an answer.

---

## 🎯 Why Use a Retriever?

- Efficiently search over large text/document datasets
- Provide LLMs with external knowledge during inference
- Combine with QA chains, agents, or memory

---

## 🧱 Core Components

| Component           | Description                                |
|---------------------|--------------------------------------------|
| `DocumentLoader`    | Loads and splits data into chunks          |
| `TextSplitter`      | Divides large documents into smaller parts |
| `Vectorstore`       | Stores and indexes embeddings              |
| `Retriever`         | Interface to search for similar chunks     |

---

## 🔍 How Retrieval Works

1. Load and split your documents
2. Embed each chunk using an LLM-backed embedding model
3. Store them in a **vector store** (like Chroma, FAISS, Pinecone)
4. Query using similarity search via a **retriever**
5. Feed results to an LLM for context-aware answers

---

## 🧪 Example: Setup a Retriever with Chroma

```python
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_community.vectorstores import Chroma
from langchain_openai import OpenAIEmbeddings
from langchain_core.documents import Document

# Sample docs
docs = [
    Document(page_content="LangChain is a powerful framework for LLM apps."),
    Document(page_content="FastAPI is great for building APIs in Python."),
    Document(page_content="Retrievers help find relevant info from documents.")
]

# Split docs into chunks
splitter = RecursiveCharacterTextSplitter(chunk_size=100, chunk_overlap=20)
chunks = splitter.split_documents(docs)

# Embed & store
embedding_model = OpenAIEmbeddings(api_key="your-api-key")
vectorstore = Chroma.from_documents(documents=chunks, embedding=embedding_model)

# Get retriever
retriever = vectorstore.as_retriever()
```

---

## 🔍 Use the Retriever in a RAG Pipeline

You can retrieve relevant docs based on a question:

```python
results = retriever.invoke("How does LangChain help LLMs?")
for doc in results:
    print(doc.page_content)
```

---

## 📦 Vector Store Options

| Vector Store | Type        | Notes                                   |
| ------------ | ----------- | --------------------------------------- |
| `Chroma`     | Local       | Easy, fast setup, great for prototyping |
| `FAISS`      | Local       | Popular open-source option              |
| `Pinecone`   | Cloud       | Scalable managed vector database        |
| `Weaviate`   | Cloud/local | Semantic search and hybrid filters      |

---

## ✅ Summary

* **Retrievers** enable LLMs to search for relevant context
* Typically backed by a vector store (e.g., Chroma, FAISS)
* Combine with chains like `RetrievalQA` or `ConversationalRetrievalChain` for powerful RAG apps

---

## 🧭 What's Next?

In [10_document_loaders.md](./10_document_loaders.md), you'll learn how to **load real-world data** into LangChain from PDFs, markdown files, websites, and more.

