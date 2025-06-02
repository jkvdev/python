# 🧠 02 — Giving Context and References in Cursor

Cursor isn’t just a code suggester — it understands your **project context**. But to get the best results, you should guide it with the right references.

This short guide covers how to give effective context when asking questions or requesting edits.

---

## 🧩 Option 1: Select Code First

**Best for:** focused edits or questions about a specific block.

1. Select the function, class, or block you want help with
2. Press `Cmd + I` (Mac) / `Ctrl + I` (Win/Linux)
3. Enter a prompt like:

   > “Add logging and type hints”
   >
   > “Make this class async-compatible”

Cursor will only consider the selected code, so this keeps the response accurate and fast.

---

## 📁 Option 2: Whole File AI Edit

**Best for:** refactors, documentation, or broad changes.

1. Open the file
2. Press `Cmd + A` to select all (or manually select)
3. Then `Cmd + I` or right-click → “Edit with AI”

Prompt examples:

> “Refactor for readability and add docstrings”
> 
> “Fix deprecated code for Python 3.12”

---

## 🔗 Option 3: Chat with Cross-File Context

**Best for:** understanding how pieces connect across the project.

Use the AI Sidebar (💬 icon or `Cmd + K`)

Prompt examples:

> “Where is `get_user_permissions()` used in this project?”
> 
> “Explain how data flows from `routes/api.py` to `services/user.py`”
> 
> “What does the overall auth flow look like?”

Cursor will consider multiple files at once, not just the one you’re viewing.

---

## 🧠 Smart Referencing Tips

* 📌 **Be explicit about filenames** when needed

  > “This function is in `utils.py`, but used in `main.py`”

* 🔍 **Use natural phrases like:**

  > “In this repo…”
  > 
  > “Across the service layer…”
  > 
  > “Between these files…”

* 📂 **Ask for overviews:**

  > “Summarize how the app starts up and initializes services”

---

## ✅ Summary

| Scenario                         | Best Reference Strategy       |
| -------------------------------- | ----------------------------- |
| Simple function/class            | Select code + `Cmd + I`       |
| Full file edit or transformation | Select file + `Cmd + I`       |
| Questions across files           | Use sidebar chat (`Cmd + K`)  |
| Project-level explanation        | Use broad prompts via sidebar |

