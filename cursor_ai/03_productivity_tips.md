# 📈 03 — Productivity Tips for Using Cursor

Cursor shines when you make it part of your daily coding workflow. These tips and tricks will help you get faster, cleaner results with less effort.

---

## ⚡ Use AI Shortcuts

* `Cmd + K` (Mac) / `Ctrl + K` (Win/Linux): **Edit selected code with AI**
  Use this for quick, inline improvements and refactors.

* `Cmd + I` (Mac) / `Ctrl + I` (Win/Linux): **Open the AI sidebar**
  Use this for chat-based interactions, cross-file reasoning, and referencing other files with `@`.

* `Cmd + Shift + P` → type “AI”: Access AI actions via the Command Palette

> 💡 Cursor's sidebar (`Cmd/Ctrl + I`) can understand and act on your full project context, not just the selected code.

---

## ✍️ Comment-Driven Prompts

You can guide Cursor using inline comments in your code:

```python
# ai: optimize this function
# ai: add type hints and docstring
```

Then select the code and press `Cmd + K` / `Ctrl + K` to let Cursor act on the comment as a natural-language instruction.

> 💡 This is great for consistent edits and automating small cleanup tasks.

---

## 🧭 Use `@` to Reference Other Files or Folders

When using the **AI sidebar** (`Cmd/Ctrl + I`), you can reference specific files or directories using `@`.

Examples:

> “Refactor this function using `@utils/formatters.py` as a guide”
>
> “Add logging similar to what's used in `@shared/logger.py`”
>
> “Rewrite based on schema in `@schemas/user.py`”

This is especially useful for making consistent changes across a codebase.

---

## 🔁 Combine Tasks in One Prompt

Cursor handles **multi-part prompts** well. Save time by combining instructions.

Examples:

> “Refactor for readability and add type hints”
>
> “Improve performance and include logging”
>
> “Convert this to async and write docstrings”

---

## 🧪 Use Cursor to Review Your Own Code

Before committing, you can ask Cursor to help check for common issues.

Examples:

> “Are any edge cases missing in this function?”
>
> “Is there unreachable or repeated logic?”
>
> “Would this scale to 10x the data volume?”

Think of it as an intelligent pre-commit reviewer.

---

## 🧠 Suggested Workflow Loop

1. 🔍 **Start in the sidebar** (`Cmd/Ctrl + I`): Ask high-level questions
2. ✍️ **Zoom in with inline edits** (`Cmd/Ctrl + K`): Focus on specific blocks
3. 💬 **Follow up in sidebar**: Ask clarifying or improvement questions

This loop helps you go from concept → code → polish, efficiently.

---

## 🚀 Bonus: Combine with External Tools

You can combine Cursor prompts with your existing toolchain:

* **Ruff formatting**

  > “Make this compliant with Ruff rules”

* **Black-style formatting**

  > “Format this file using Black’s style guide”

* **FastAPI/Django integration**

  > “Create endpoints using the schema in `@schemas/user.py`”
  > “Add Pydantic validation and docstrings to this route”

---

## ✅ Summary Tips

| Tip                           | Shortcut / Method             |
| ----------------------------- | ----------------------------- |
| Inline edit selected code     | `Cmd + K` / `Ctrl + K`        |
| Sidebar chat, file references | `Cmd + I` / `Ctrl + I`        |
| AI actions from palette       | `Cmd + Shift + P` → "AI"      |
| Comment-style prompts         | `# ai: describe purpose`      |
| Cross-file context (`@`)      | Use in sidebar with `Cmd + I` |
