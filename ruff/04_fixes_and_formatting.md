# 🧹 Fixes and Formatting

Ruff can automatically fix many lint issues and format your Python code in a consistent, opinionated style — combining functionality from tools like `black`, `isort`, and `autoflake`.

---

## 🔧 Auto-Fixing Lint Issues

To automatically fix issues that Ruff detects:

```bash
ruff check . --fix
```

This applies safe, non-destructive fixes, such as:

- Removing unused imports (`F401`)
- Reordering imports (`I001`)
- Cleaning up unused variables (`F841`)

You can also display which specific fixes were applied:

```bash
ruff check . --fix --show-fixes
```

---

## 🎨 Code Formatting

Ruff includes a built-in formatter (like `black`) you can use with:

```bash
ruff format .
```

To format a specific file:

```bash
ruff format app/utils.py
```

---

## ⚙️ Formatting Options

Ruff respects formatting-related options from your `pyproject.toml`. For example:

```toml
[tool.ruff]
line-length = 100
indent-width = 4
```

You can fine-tune formatting and linting behavior together from one config file.

---

## 🚫 What Ruff Won’t Fix

Ruff only applies **safe** and **deterministic** fixes. It won’t:

- Refactor complex logic
- Rename variables
- Remove unused functions
- Auto-convert syntax for breaking changes

For things it *can’t* fix, Ruff will still report the issue, so you can handle it manually.

---

## 🧠 Summary of Fixable Examples

| Rule Code   | Description                              |
| ----------- | ---------------------------------------- |
| F401        | Unused import                            |
| F841        | Unused variable                          |
| I001        | Imports not correctly sorted             |
| E701        | Multiple statements on one line          |
| E711        | Comparison to `None` should be `is`      |

You can also combine linting and formatting in one run:

```bash
ruff check . --fix && ruff format .
```

---

Next up: see how Ruff organizes its linting rules and categories in [`05_linters_and_rules.md`](05_linters_and_rules.md). 🧠

