# 🧠 Linters and Rules

Ruff comes with over 500 built-in linting rules, organized into logical categories. These rules help catch common errors, enforce style consistency, and clean up code automatically.

---

## 📦 Rule Categories

Rules are grouped by code prefixes (similar to Flake8-style). Here are some common categories:

| Prefix | Description               |
|--------|----------------------------|
| F      | Pyflakes (e.g. unused imports, undefined names) |
| E      | pycodestyle (e.g. indentation, whitespace)      |
| W      | Warning-level style rules                       |
| I      | isort (import sorting)                          |
| D      | pydocstyle (docstring conventions)              |
| N      | pep8-naming (naming conventions)                |
| UP     | pyupgrade (Python version syntax updates)       |
| C4     | flake8-comprehensions (comprehension simplification) |

You can find the [full list of rules here](https://docs.astral.sh/ruff/rules/).

---

## ✅ Enabling Specific Rules

Use the `select` option in your config to include only certain rule codes or categories:

```toml
[tool.ruff]
select = ["F", "E", "I"]
```

Or enable individual rules explicitly:

```toml
[tool.ruff]
select = ["F401", "E501"]
```

---

## 🚫 Ignoring Rules

You can disable rules globally using `ignore`:

```toml
[tool.ruff]
ignore = ["E501", "D100"]
```

You can also ignore rules for specific files:

```toml
[tool.ruff.per-file-ignores]
"tests/*.py" = ["D", "S101"]
```

---

## 🔍 Checking Specific Rules Only

If you want to run Ruff temporarily with only specific rules:

```bash
ruff check . --select F401
```

You can also combine this with `--fix`:

```bash
ruff check . --select I001 --fix
```

---

## 🧠 Tips

- Use `"ALL"` to enable every available rule (not always recommended):

  ```toml
  select = ["ALL"]
  ```
- Combine `select` and `ignore` to fine-tune behavior:

  ```toml
  select = ["F", "E", "I"]
  ignore = ["E501"]
  ```

---

In the final section, we'll go over some handy tips, commands, and editor integrations in [`06_tips_and_tricks.md`](06_tips_and_tricks.md). 🎯

