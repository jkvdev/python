# 🧬 Embeddings and Vectorstores in LangChain

**Embeddings** turn text into numerical vectors that capture meaning. This allows us to **search, compare, and retrieve** similar pieces of text based on semantic meaning—not just keywords.

In LangChain, embeddings are used with **vectorstores** to enable tasks like document search and RetrievalQA.

---

## 🧠 Why Use Embeddings?

* Match questions with **relevant text** from your data
* Find similarity between documents, sentences, or queries
* Power RAG pipelines, search tools, semantic clustering
* Foundation for RetrievalQA, chat over docs, and more

---

## 🧬 What Is an Embedding?

An **embedding** is a list of numbers (a vector) that represents the **semantic meaning** of a piece of text.

For example:

```text
"How to bake a cake?" → [0.01, -0.32, 0.12, ...]
```

Texts with similar meanings will have vectors that are **close together** in this space.

---

## 🛠️ Embedding Example with OpenAI

```python
from langchain_openai import OpenAIEmbeddings

embedding_model = OpenAIEmbeddings(api_key="your-api-key")

text = "How to make pancakes?"
embedding = embedding_model.embed_query(text)

print(embedding[:5])  # Shows first 5 values in the vector
```

---

## 🧱 Using Embeddings with Documents

To use embeddings in workflows, you usually:

1. **Split** your documents into chunks
2. **Embed** each chunk
3. **Store** them in a **vectorstore**
4. Use a **retriever** to get relevant chunks for a query

---

## 💾 Vectorstore Example with Chroma

```python
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

vectorstore.persist()  # Optional: persist to disk for reuse
```

Now you can **retrieve relevant chunks** based on a user query:

```python
retriever = vectorstore.as_retriever()
results = retriever.get_relevant_documents("How to make a sandwich?")  # Returns top-k similar chunks
```

---

## 🔍 How Similarity Works

Vectorstores use **cosine similarity** (or other math) to find chunks **closest in meaning** to the query vector. This is how it knows which parts of your notes to bring into the LLM's context.

---

## 📦 Other Vectorstores You Can Use

| Vectorstore                 | Description                                     |
| --------------------------- | ----------------------------------------------- |
| `Chroma`                    | In-memory, good for local/dev use               |
| `FAISS`                     | Fast, offline similarity search                 |
| `Pinecone`                  | Cloud-hosted, scalable + persistent             |
| `Weaviate`, `Qdrant`, etc.  | Specialized for large-scale, production search  |

---

## 🔁 When to Re-Embed

You should re-run the embedding step when:

* You add new documents
* You change the chunking logic
* You switch to a different embedding model

---

## ✅ Summary

* **Embeddings** convert text into vectors so we can compare meaning
* Used in **vectorstores** to build retrievers and semantic search
* Enable key features like **RetrievalQA**, search, chat over docs
* You can embed chunks with OpenAI and store them in tools like **Chroma**

---

## 🧭 What's Next?

If you're curious how all of this fits into RetrievalQA, revisit [12_retrieval_qa.md](./12_retrieval_qa.md) to see embeddings in action!

