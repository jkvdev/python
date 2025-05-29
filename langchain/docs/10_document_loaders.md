# 📥 Document Loaders in LangChain

**Document loaders** let you read and parse data from various sources (PDFs, text files, HTML, Notion, APIs, etc.) into `Document` objects, which you can then split and embed for use in retrieval or RAG applications.

---

## 🎯 Why Use Document Loaders?

- Pull in unstructured data from local or web sources
- Convert content into a format LangChain can process
- Combine with text splitters, retrievers, and QA chains

---

## 🧱 Anatomy of a Loaded Document

Each document is represented like this:

```python
Document(
    page_content="actual text content...",
    metadata={"source": "source_info"}
)
```

You can filter or track documents by their metadata.

---

## 🔧 Installing Required Packages

```bash
pip install unstructured pdfminer.six html2text
```

* `unstructured` – Handles complex formats like PDFs, DOCX, HTML
* `pdfminer.six` – PDF parsing backend
* `html2text` – HTML to Markdown conversion

---

## 🧪 Example: Load a PDF File

```python
from langchain_community.document_loaders import PyPDFLoader

loader = PyPDFLoader("example.pdf")
docs = loader.load()

print(docs[0].page_content[:300])  # View sample content
```

> 💡 **Tip:** Some loaders (like `PyPDFLoader`) automatically split by page. Others (like `TextLoader`) return one document per file.

---

## 🧪 Example: Load a Markdown or Text File

```python
from langchain_community.document_loaders import TextLoader

loader = TextLoader("notes.md", encoding="utf-8")
docs = loader.load()
```

---

## 🧪 Example: Load a Web Page

```python
from langchain_community.document_loaders import WebBaseLoader

loader = WebBaseLoader("https://en.wikipedia.org/wiki/LangChain")
docs = loader.load()
```

---

## 🧪 Example: Load a Folder of Files

```python
from langchain_community.document_loaders import DirectoryLoader

loader = DirectoryLoader(
    "./my-documents",
    glob="**/*.txt",             # All .txt files recursively
    loader_cls=TextLoader
)

docs = loader.load()
```

---

## 🧪 Bonus: Filter by Metadata

You can filter documents based on metadata fields, for example:

```python
filtered_docs = [
    doc for doc in docs 
    if "summary" in doc.metadata.get("source", "")
]
```

---

## ➕ Post-Loading: Text Splitting

Documents are often long, so you split them into chunks:

```python
from langchain.text_splitter import RecursiveCharacterTextSplitter

splitter = RecursiveCharacterTextSplitter(chunk_size=500, chunk_overlap=50)
chunks = splitter.split_documents(docs)
```

These chunks are what get embedded and stored in vector databases.

---

## ✅ Summary

* **Document loaders** bring in real-world data
* Supports PDF, HTML, text, Notion, directories, and more
* Combine with **text splitters** → **embeddings** → **retrievers**
* Enables full RAG pipelines in LangChain

---

## 🧭 What's Next?

In [11_tools_and_agents.md](./11_tools_and_agents.md), we'll look at how to equip your LLM with **tools and reasoning capabilities** using LangChain Agents.

