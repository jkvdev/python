# 🧯 Common Issues and Troubleshooting

This guide covers typical problems you might encounter while using Poetry — and how to fix them.

---

## ❌ Poetry Command Not Found

#### Problem

Running `poetry` shows a “command not found” error.

#### Solution

Ensure Poetry’s installation path is added to your system’s `PATH`.

**On Windows:**
Check that this path is in your environment variables:
`C:\Users\<YourName>\AppData\Roaming\Python\Scripts`

Test it with:

```powershell
poetry --version
```

---

## 🐍 Wrong Python Version Being Used

#### Problem

Poetry is using a different Python version than expected.

#### Solution

Set the correct Python version explicitly:

```bash
poetry env use python3.11
```

Verify with:

```bash
poetry run python --version
```

---

## 📦 Dependencies Not Installing

#### Problem

You run `poetry install`, but dependencies fail to install or are missing.

#### Solution

Reset the virtual environment:

```bash
poetry env remove python
poetry install
```

Still not working? Check for typos or version conflicts in your `pyproject.toml`.

---

## 🔁 Can't Publish: Version Already Exists

#### Problem

Publishing fails with an error like *“HTTP 400: File already exists”*.

#### Solution

Bump your version before trying again:

```bash
poetry version patch
poetry publish --build
```

---

## 🧪 `ModuleNotFoundError` Inside VS Code

#### Problem

Your code works with `poetry run` but fails in VS Code (e.g., can't find installed packages).

#### Solution

Ensure VS Code is using the correct virtual environment:

1. Run `poetry env info --path` to get the venv path.
2. Open VS Code → `Ctrl+Shift+P` → **Python: Select Interpreter**
3. Choose the environment path from step 1.

---

## 📘 Related Topics

* [Installation & Project Setup](02_project_setup.md)
* [Virtual Environment Handling](05_virtualenv_handling.md)

