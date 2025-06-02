# ⚙️ Installation and Project Setup

This guide covers how to use Poetry in real-world projects — whether you're starting a new one or adding Poetry to an existing codebase.

---

## 🆕 Creating a New Project

Poetry can scaffold a new Python project with one command:

```bash
poetry new my_project
```

This creates a directory structure like:

```bash
my_project/
├── pyproject.toml
├── my_project/
│   └── __init__.py
└── tests/
    └── test_my_project.py
```

By default, the `pyproject.toml` includes project metadata like name, version, description, author, and Python version.

To enter the project folder and start working:

```bash
cd my_project
```

---

## 🧱 Adding Poetry to an Existing Project

If you're working with an existing project, you can initialize Poetry manually:

```bash
poetry init
```

This walks you through creating a `pyproject.toml`. You can:

* Accept defaults
* Add dependencies interactively
* Leave it blank and add them later

After generating the `pyproject.toml`, run:

```bash
poetry install
```

This creates a virtual environment and installs any dependencies (if present).

---

## 📝 Customizing `pyproject.toml`

After setup, you can edit the `pyproject.toml` directly. Example:

```toml
[tool.poetry]
name = "my_project"
version = "0.1.0"
description = "A sample Python project using Poetry"
authors = ["Your Name <you@example.com>"]
readme = "README.md"
packages = [{ include = "my_project" }]

[tool.poetry.dependencies]
python = "^3.10"
requests = "^2.31.0"

[tool.poetry.dev-dependencies]
pytest = "^8.0.0"
```

---

## 📂 Project Structure: What Each File Does

| File             | Purpose                                             |
| ---------------- | --------------------------------------------------- |
| `pyproject.toml` | Project config (metadata, dependencies, build info) |
| `poetry.lock`    | Auto-generated lock file for reproducible installs  |
| `my_project/`    | Your actual Python code                             |
| `tests/`         | Unit tests (created by default)                     |

---

## ✅ Next Steps

Once set up, you can:

```bash
poetry add package_name          # Add a dependency
poetry run python your_script.py  # Run code inside the venv
poetry shell                     # Spawn a subshell with the venv activated
```

For more, see the [Dependency Management](04_dependency_management.md) section.

