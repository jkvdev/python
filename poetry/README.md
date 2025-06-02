# 📦 Poetry: Python Dependency & Packaging Tool

**Poetry** is a modern tool for managing Python projects, handling dependencies, packaging, and publishing — all in one place. It provides a streamlined, repeatable way to manage Python environments using a declarative configuration file.

---

## 🚀 What is Poetry?

Poetry is a dependency manager and packaging tool for Python that uses the standardized `pyproject.toml` file to define project metadata, dependencies, scripts, and build settings.

> “Poetry helps you declare, manage and install dependencies of Python projects, ensuring you have a reliable and repeatable environment.” — Poetry docs

---

## 🤔 Why Use Poetry?

- ✅ Single source of truth via `pyproject.toml`  
- ✅ Simplified package publishing  
- ✅ Reproducible builds with `poetry.lock`  
- ✅ Built-in virtual environment support  
- ✅ Clean, user-friendly CLI  

---

## 🔧 Installation

### 🪟 Windows

Run the following command in **PowerShell (Windows Terminal)**:

```powershell
(Invoke-WebRequest -Uri https://install.python-poetry.org -UseBasicParsing).Content | python -
```

> Make sure Python is in your PATH, and use an elevated terminal if needed (Run as Administrator).

Once installed, add Poetry’s install path to your environment variable if it isn’t detected:

```powershell
[Environment]::SetEnvironmentVariable("Path", [Environment]::GetEnvironmentVariable("Path", "User") + ";C:\Users\<YourUsername>\AppData\Roaming\Python\Scripts", "User")
```

Replace `<YourUsername>` with your actual Windows username.

---

### 🐧 Linux / 💻 macOS

Use this command:

```bash
curl -sSL https://install.python-poetry.org | python3 -
```

Make sure `~/.local/bin` is in your system's `PATH`.

📘 Official Docs: [Poetry Installation](https://python-poetry.org/docs/#installation)

---

## 📁 Project Structure Example

A basic Poetry project structure looks like this:

```bash
my_project/
├── pyproject.toml
├── poetry.lock
├── my_project/
│   └── __init__.py
└── tests/
    └── test_basic.py
```

---

## 🧪 Basic Usage

```bash
poetry new my_project
cd my_project
poetry add requests
poetry install
poetry run python script.py
```

---

## 📚 Documentation Contents

* [`01_poetry_vs_pip.md`](01_poetry_vs_pip.md) — Comparing Poetry with pip, pipenv, and virtualenv
* [`02_installation_and_setup.md`](02_installation_and_setup.md) — Installation, initialization, and configuration
* [`03_pyproject_toml.md`](03_pyproject_toml.md) — Understanding the `pyproject.toml` file
* [`04_dependency_management.md`](04_dependency_management.md) — Adding, updating, and removing dependencies
* [`05_virtualenv_handling.md`](05_virtualenv_handling.md) — How Poetry manages virtual environments
* [`06_publishing_packages.md`](06_publishing_packages.md) — Building and publishing Python packages
* [`07_common_commands.md`](07_common_commands.md) — Reference of commonly used Poetry commands
* [`08_troubleshooting.md`](08_troubleshooting.md) — Common problems and their solutions

---

## 🎯 Objective

Provide a clear and practical reference for using Poetry effectively in Python projects, suitable for developers ranging from beginner to intermediate levels.

