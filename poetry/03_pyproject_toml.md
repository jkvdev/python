# 📄 Understanding `pyproject.toml`

The `pyproject.toml` file is the central configuration file used by Poetry. It defines the project's metadata, dependencies, build settings, and more — all in a single, standardized format.

This file is part of [PEP 518](https://peps.python.org/pep-0518/), which introduced a standard way to specify build systems for Python projects.

---

## 🧠 Why `pyproject.toml`?

Before `pyproject.toml`, Python projects often used multiple files:

- `setup.py`
- `requirements.txt`
- `MANIFEST.in`

Poetry replaces all of them with a single `pyproject.toml`, improving maintainability and consistency.

---

## 🧱 Basic Structure

Here’s a minimal example:

```toml
[tool.poetry]
name = "my_project"
version = "0.1.0"
description = "A simple project"
authors = ["Your Name <you@example.com>"]
readme = "README.md"
packages = [{ include = "my_project" }]

[tool.poetry.dependencies]
python = "^3.10"
requests = "^2.31.0"

[tool.poetry.dev-dependencies]
pytest = "^8.0.0"

[build-system]
requires = ["poetry-core"]
build-backend = "poetry.core.masonry.api"
```

---

## 🔍 Sections Breakdown

### `[tool.poetry]`

Defines core project metadata:

| Field         | Description                                   |
| ------------- | --------------------------------------------- |
| `name`        | Package name (must match the folder name)     |
| `version`     | Semantic version (e.g., `0.1.0`)              |
| `description` | A short summary of the project                |
| `authors`     | List of author names and emails               |
| `readme`      | Optional: points to the README file           |
| `packages`    | Optional: what package(s) to include in build |

---

### `[tool.poetry.dependencies]`

Lists required dependencies. Specify versions using caret (`^`) by default, e.g.:

```toml
[tool.poetry.dependencies]
python = "^3.10"
requests = "^2.31.0"
```

You can also pin exact versions (`==`), use comparison operators (`>=`, `<`), or add extras, Git, and path-based dependencies.

---

### `[tool.poetry.dev-dependencies]`

These are packages used during development only (e.g., testing or linting tools):

```toml
[tool.poetry.dev-dependencies]
pytest = "^8.0.0"
black = "^24.0.0"
```

---

### `[build-system]`

This is required by PEP 517/518 to specify how the project is built.

```toml
[build-system]
requires = ["poetry-core"]
build-backend = "poetry.core.masonry.api"
```

This tells Python tooling how to build your project using Poetry.

---

## ✅ Tips

* Poetry automatically updates this file when you use commands like `poetry add` or `poetry remove`.
* You can safely edit the file manually for things like metadata or script definitions.
* Avoid manually changing `poetry.lock`; it’s managed by Poetry.

---

## 📘 Related Topics

* [Dependency Management](04_dependency_management.md)
* [Publishing Packages](06_publishing_packages.md)

