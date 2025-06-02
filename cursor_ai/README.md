# 🧠 Cursor AI — Beginner-Friendly Documentation

### 📌 What is Cursor?

**Cursor** is an AI-enhanced code editor built on top of **VSCode**, offering integrated AI coding assistance. It’s designed to boost developer productivity by helping you write, edit, refactor, and understand code faster — without leaving your editor.

> ⚡️ Cursor uses advanced language models like **GPT-4o** and **Claude** (depending on your plan and preferences) to power its features.

---

## 🚀 Key Features

* 🧠 **AI-Powered Autocomplete**
* ✍️ **Inline AI Edits**
* 💬 **Chat with your code**
* 🔍 **Understand unfamiliar codebases**
* 🛠️ **Refactor with natural language**
* 🧪 **Ask questions about tests and logic**
* 🔄 **Edit multiple files via AI**

---

## ⚙️ Installation & Setup

#### Option 1: Download Cursor

* Go to [cursor.sh](https://www.cursor.sh/)
* Click **Download** for macOS, Windows, or Linux
* Install it just like VSCode

#### Option 2: From Terminal (macOS)

```bash
brew install --cask cursor
```

#### Log in

* Open the app
* Sign in with GitHub or Google to activate full AI functionality

> ✨ Free plan includes basic AI usage. Pro plan unlocks more compute and access to GPT-4o.

---

## ✨ Getting Started

#### 1. Open a Project Folder

Just like in VSCode, you can open any local folder or clone a repo.

#### 2. Use the AI Sidebar

Click the 💬 icon or press `Cmd + K` (Mac) / `Ctrl + K` (Windows/Linux) to open the AI sidebar chat.

#### 3. Ask Cursor Something

Examples:

* “What does this function do?”
* “Can you refactor this code to use async/await?”
* “Write unit tests for this class.”

#### 4. Inline Edits

Select code → Right-click → “Edit with AI”
Or press `Cmd + I` / `Ctrl + I`

Examples:

* “Add logging”
* “Convert this to a class”
* “Improve performance”

---

### 🛠️ Common Use Cases

#### ✅ Understanding Code

> “What is this file doing?”
> “Explain the data flow in this function.”

#### 🧪 Writing Tests

> “Write pytest cases for this function”
> “Generate edge case tests for this API”

#### ♻️ Refactoring

> “Refactor this to follow clean architecture”
> “Split this into smaller functions”

#### 📄 Documentation

> “Add docstrings to all functions in this file”
> “Generate markdown docs for this module”

#### 🔗 Multi-file Reasoning

> Cursor understands context across multiple files.
> For example, you can ask about a function defined in `utils.py`, and Cursor will analyze how it’s used in `main.py` and `routes/api.py`.

---

### 🧩 Differences from Copilot / VSCode

| Feature                 | Cursor                    | GitHub Copilot         |
| ----------------------- | ------------------------- | ---------------------- |
| Autocomplete            | ✅ Yes (GPT-powered)       | ✅ Yes                  |
| Full file edits         | ✅ Yes                     | ❌ No                   |
| Inline refactor         | ✅ Yes (natural language)  | ❌ No                   |
| Project-wide reasoning  | ✅ Yes                     | ❌ Limited              |
| AI chat                 | ✅ Built-in                | 🟡 Requires extension  |
| Based on VSCode         | ✅ Yes                     | ✅ Yes                  |

---

### 💡 Tips

* Use `Cmd/Ctrl + K` for quick AI access
* Prefix requests with “explain”, “refactor”, “test”, “optimize”, or “document”
* Select code and press `Cmd + I` to edit it with AI (works even for full files!)
* Use inline comments like `// ai: optimize this` in supported contexts
* Ask for visualizations: “Draw a diagram of the class structure”
* Try working entirely in Cursor for a few days to feel the difference

---

### 🔒 Notes on Privacy and Licensing

* Cursor is a **closed-source** tool.
* It relies on **cloud-based AI models**, so an internet connection is required.
* Avoid using Cursor for codebases with strict privacy/confidentiality requirements unless you're comfortable with its data policy.

---

### 📚 Resources

* [Official Site](https://www.cursor.sh/)
* [Cursor on X/Twitter](https://twitter.com/cursor)
* [Cursor GitHub Issues](https://github.com/cursor-dev/issues)
* [AI Prompts Cheatsheet](https://docs.cursor.sh/ai-cheatsheet)
