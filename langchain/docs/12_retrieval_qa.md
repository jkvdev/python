# 🔍 RetrievalQA in LangChain

**RetrievalQA** is a powerful chain that enables **question-answering over documents** by integrating a retriever with an LLM. It's the backbone of **Retrieval-Augmented Generation (RAG)**—a method where an LLM uses external data to answer user queries.

---

## 🎯 Why Use RetrievalQA?

- Answer questions using **your own data**
- Combine document context with LLM power
- Prevent hallucinations by grounding output in facts
- Simplify RAG setup with just one line of chain composition

---

## 🧠 How RetrievalQA Works

1. A **retriever** finds the most relevant chunks of text for a given question  
2. The chunks are **passed to an LLM** as additional context  
3. The LLM generates an answer based on both the context and question

---

## 🔧 Quick Setup Example

```python
from langchain_openai import ChatOpenAI, OpenAIEmbeddings
from langchain.chains import RetrievalQA
from langchain_community.vectorstores import Chroma
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_community.document_loaders import TextLoader

# Load and split documents
loader = TextLoader("notes.md", encoding="utf-8")
docs = loader.load()

splitter = RecursiveCharacterTextSplitter(chunk_size=500, chunk_overlap=50)
chunks = splitter.split_documents(docs)

# Embed and store
embedding_model = OpenAIEmbeddings(api_key="your-api-key")
vectorstore = Chroma.from_documents(chunks, embedding=embedding_model)
retriever = vectorstore.as_retriever()

# LLM model
llm = ChatOpenAI(api_key="your-api-key")

# Create RetrievalQA chain
qa_chain = RetrievalQA.from_chain_type(
    llm=llm,
    retriever=retriever,
    return_source_documents=True
)

# Ask a question
query = "What are the main ideas in the notes?"
result = qa_chain.invoke({"query": query})

print("Answer:", result["result"])
print("Sources:")
for doc in result["source_documents"]:
    print("-", doc.metadata.get("source", "Unknown"))
    # Tip: You can also inspect doc.page_content for full text
```

---

## 🔍 Options for `.from_chain_type()`

| Parameter                 | Description                                             |
| ------------------------- | ------------------------------------------------------- |
| `llm`                     | The language model to use                               |
| `retriever`               | A retriever object (from vector store)                  |
| `chain_type`              | How context is formatted ("stuff", "map\_reduce", etc.) |
| `return_source_documents` | Include sources in the output                           |

> 📝 `chain_type` defaults to `"stuff"` if not specified.

---

## 🧭 Chain Types

| Chain Type     | Behavior                              |
| -------------- | ------------------------------------- |
| `"stuff"`      | Combine all documents into one prompt |
| `"map_reduce"` | Answer each chunk, then summarize     |
| `"refine"`     | Iteratively refine an answer          |

---

## ⚙️ Use Cases

* Chat with PDFs, Markdown, Notion pages
* Internal company knowledgebases
* Customer support automation
* Legal and scientific document search

---

## ✅ Summary

* `RetrievalQA` lets you ask questions about documents
* Combines a retriever and an LLM into one chain
* Supports multiple context formats and output options
* Great for document-based chat, RAG apps, and more

---

## 🧭 What's Next?

In [13_multimodal_and_custom_tools.md](./13_multimodal_and_custom_tools.md), we'll explore how to use **multi-modal inputs** and create **custom tools** that agents and chains can use.

