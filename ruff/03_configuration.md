# ⚙️ Configuration

The recommended way to configure Ruff is using the `pyproject.toml` file, allowing you to define project-specific rules, formatting behavior, exclusions, and more.

---

## 📝 Basic Example

Here’s a minimal `pyproject.toml` setup:

```toml
[tool.ruff]
line-length = 88
select = ["F", "E", "I"]
ignore = ["E501"]
exclude = ["migrations", "tests/fixtures"]
```

---

## 🔧 Common Settings

| Option            | Description                                        |
| ----------------- | -------------------------------------------------- |
| `line-length`     | Max line length for formatting/linting             |
| `select`          | List of rule codes/categories to check             |
| `ignore`          | Rules to ignore (even if they’re selected)         |
| `exclude`         | Directories or files to skip                       |
| `extend-exclude`  | Additional paths to exclude (appended to default)  |
| `target-version`  | Target Python version (e.g. `"py310"`)             |

Example:

```toml
[tool.ruff]
target-version = "py310"
line-length = 100
select = ["ALL"]
ignore = ["D100", "D101"]
```

---

## 🧩 Configuration Placement

Make sure your `pyproject.toml` is at the root of your project:

```
your-project/
├── pyproject.toml  👈
├── app/
├── tests/
└── ...
```

Ruff will automatically detect and apply the config when run from within the project directory.

---

## 📁 Per-File Ignores (Optional)

You can ignore specific rules for certain files using this format:

```toml
[tool.ruff.per-file-ignores]
"tests/test_*.py" = ["D", "S101"]
"scripts/*.py" = ["F401"]
```

---

Now that Ruff is configured for your project, let’s explore how it handles auto-fixing and formatting in [`04_fixes_and_formatting.md`](04_fixes_and_formatting.md). 🧹

