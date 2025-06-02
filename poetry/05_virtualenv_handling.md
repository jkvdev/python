# 🧪 Virtual Environment Handling in Poetry

Poetry automatically manages virtual environments for Python projects. This simplifies setup and keeps project dependencies isolated from the global Python environment.

---

## ⚙️ How It Works

When you run a command like:

```bash
poetry install
```

Poetry will:

1. Create a virtual environment (if it doesn't already exist)
2. Install all dependencies into it
3. Link the environment to your project

By default, the environment is stored in a cache directory outside your project folder (e.g., `~/.cache/pypoetry/virtualenvs` on Unix-like systems).

---

## 📍 Viewing the Environment Path

To check where the virtual environment is located:

```bash
poetry env info --path
```

This returns the full path to the virtual environment Poetry created for the project.

---

## 💻 Activating the Environment Manually

To activate the environment manually (useful for debugging or direct package inspection):

```bash
poetry shell
```

This opens a new shell session with the virtual environment activated. To exit:

```bash
exit
```

---

## 🚀 Running Commands Without Activating

You don’t need to activate the environment to run code. Use:

```bash
poetry run python script.py
poetry run pytest
```

This ensures you're using the correct Python and dependencies without modifying your shell.

---

## 🔄 Recreating the Environment

To recreate the virtual environment from scratch:

```bash
poetry env remove python
poetry install
```

This deletes the existing environment and reinstalls everything.

---

## ⚙️ Configuration Options

Customize how Poetry manages environments:

### Enable or disable virtual environments:

```bash
poetry config virtualenvs.create true   # Enable (default)
poetry config virtualenvs.create false  # Use system interpreter
```

### Store environments inside the project:

```bash
poetry config virtualenvs.in-project true
```

This creates a `.venv/` folder inside the project directory.

To revert to Poetry's default behavior (global cache):

```bash
poetry config --unset virtualenvs.in-project
```

---

## 🔍 Troubleshooting Tips

* To use a specific Python version:

  ```bash
  poetry env use python3.11
  ```

* To list all environments managed by Poetry:

  ```bash
  poetry env list
  ```

* If you manually delete the `.venv/` folder, run:

  ```bash
  poetry install
  ```

  to regenerate it.

---

## 📘 Related Topics

* [Dependency Management](04_dependency_management.md)
* [Publishing Packages](06_publishing_packages.md)

