# ⚙️ 02 - Installation and Setup

## 📦 Step 1: Create a Virtual Environment (Recommended)

Using a virtual environment keeps your project dependencies isolated.

### For macOS/Linux:

```bash
python3 -m venv venv
source venv/bin/activate
```

### For Windows:

```bash
python -m venv venv
venv\Scripts\activate
```

---

## 📥 Step 2: Install FastAPI and Uvicorn

Use `pip` to install the core dependencies:

```bash
pip install fastapi uvicorn[standard]
```

- `fastapi`: The web framework
- `uvicorn[standard]`: The ASGI server that runs your app (with extra features)

---

## 🚀 Step 3: Write a Minimal App

Create a file like `main.py`:

```python
from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def read_root():
    return {"message": "Hello, FastAPI!"}
```

---

## ▶️ Step 4: Run the App

There are **two ways** to run your FastAPI app:

### ✅ Option A: Recommended (FastAPI ≥ 0.111.0)

If you're using a newer version of FastAPI, you can use the new built-in development server:

```bash
fastapi dev main.py
```

This is a convenient shorthand and includes features like hot-reload.

---

### ⚙️ Option B: Traditional Uvicorn

This works in all versions:

```bash
uvicorn main:app --reload
```

- `main`: The filename (without `.py`)
- `app`: The FastAPI app instance (`app = FastAPI()`)
- `--reload`: Automatically restarts the server on code changes

---

## 🌐 Step 5: Explore Interactive API Docs

Once running, visit:

- Swagger UI: [http://localhost:8000/docs](http://localhost:8000/docs)
- ReDoc: [http://localhost:8000/redoc](http://localhost:8000/redoc)

These docs are **auto-generated** by FastAPI based on your routes and type hints.

---

## 📁 Bonus Tip: Recommended Project Structure

```plaintext
your-project/
├── main.py
├── requirements.txt
├── learning_notes/
└── venv/ (not pushed to GitHub)
```

You can generate your `requirements.txt` with:

```bash
pip freeze > requirements.txt
```

---

## ✅ Summary

To get started with FastAPI:

1. Use a virtual environment
2. Install FastAPI and Uvicorn
3. Define routes in a Python file
4. Run it using `uvicorn`
5. Explore your API in auto-generated docs

This setup prepares you to build and iterate quickly with clean, documented APIs.
