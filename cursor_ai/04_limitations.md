# 🚧 04 — Limitations and Considerations When Using Cursor

While Cursor is a powerful AI-enhanced editor, it's important to understand its current limitations and usage boundaries to avoid surprises or misuse.

---

## 🔒 Cloud-Based, Not Local

Cursor relies on cloud-based language models like GPT-4o or Claude. This means:

* ❌ **No offline AI features** — an internet connection is required
* 🔐 **Code is sent to external servers** for processing
* ⚠️ **Not suitable for sensitive, private, or proprietary code** unless you’re confident in their data practices

> **🧠 Tip:** Use Cursor freely for learning, open-source, personal projects, and exploratory refactors — avoid it for NDA or client-protected codebases.

---

## 🧠 Model Limitations

Cursor uses large language models, which have the following known behaviors:

* May **hallucinate answers** or invent functions that don't exist
* Can occasionally **miss context** in highly dynamic or deeply abstract code
* Does not understand **external APIs** unless included in the prompt or file

> 💡 Always review AI output before committing. It’s helpful — not infallible.

---

## ⚠️ Multi-File Edits Can Be Tricky

Cursor can reason across files using the sidebar, but:

* AI inline edits (`Cmd/Ctrl + K`) work on **selected code only**
* Sidebar prompts (`Cmd/Ctrl + I`) allow **cross-file awareness**, but the quality depends on:

  * Clarity of your prompt
  * Size and layout of your repo
  * References provided using `@filename` or `@folder`

---

## 💬 Prompt Sensitivity

Like any LLM-powered tool, results can vary based on phrasing.

* ✅ “Refactor for readability and performance” → Great
* ❌ “Make it better” → Too vague
* ✅ “Add type hints and docstrings to all functions in this file” → Precise and effective

---

## ⏱️ Performance & Limits

* Heavy prompts or large files may take longer or timeout
* There are **usage limits** depending on your plan (especially on free tier)
* Cursor may use different models (GPT-4o, Claude) depending on context and availability

---

## 🧪 No Formal Type Checking or Execution

Cursor does not **run**, **test**, or **type-check** your code. It only suggests changes based on language models.

> ✅ Combine with tools like `pytest`, `ruff`, `pyright`, or `black` for robust workflows.

---

## ✅ Summary

| Limitation                   | Notes & Mitigation                                |
| ---------------------------- | ------------------------------------------------- |
| Cloud-based AI               | Don’t use with sensitive/private code             |
| No offline support           | Requires active internet connection               |
| AI may hallucinate           | Always review suggestions manually                |
| Prompt sensitivity           | Be clear and specific in your requests            |
| No real execution or testing | Use external tools like pytest, ruff, black, etc. |
| Usage limits on free plan    | Consider upgrading if needed for heavier usage    |

