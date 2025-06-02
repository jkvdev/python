# 🎯 Tips and Tricks

This section includes helpful commands, shortcuts, and editor integrations to get the most out of Ruff in your workflow.

---

## 🖥️ VS Code Integration

Install the [Ruff extension for VS Code](https://marketplace.visualstudio.com/items?itemName=charliermarsh.ruff):

1. Open the Extensions sidebar (`Ctrl+Shift+X`)
2. Search for “Ruff” and install
3. Make sure it's enabled for your workspace

### 📚 VS Code Commands (Command Palette)

Use `Ctrl+Shift+P` to open the Command Palette and run:

- `Ruff: Check current file`
- `Ruff: Format current file`
- `Ruff: Restart server`
- `Ruff: Show output`

To use Ruff as the default formatter, add this to your settings:

```json
"python.formatting.provider": "ruff",
"editor.formatOnSave": true
```

You may also want to disable conflicting tools:

```json
"python.linting.pylintEnabled": false,
"python.linting.flake8Enabled": false
```

---

## 🧪 Pre-commit Hook

To run Ruff before every commit, use the `pre-commit` framework.

1. Install pre-commit:

```bash
pip install pre-commit
```

2. Add a `.pre-commit-config.yaml` file:

```yaml
repos:
  - repo: https://github.com/astral-sh/ruff-pre-commit
    rev: v0.4.3  # Use the latest version (or "latest")
    hooks:
      - id: ruff
      - id: ruff-format
```

3. Install the hook:

```bash
pre-commit install
```

Now Ruff will check and format your code before each commit.

---

## 📁 Ignore Files and Directories

Use `.ruffignore` to manually ignore paths without changing config:

```
# .ruffignore
scripts/
old_code/
tests/fixtures/test_data.py
```

This can be helpful when experimenting locally or ignoring temporary code.

---

## 🔁 Run Ruff Automatically

You can add a script to your project’s `Makefile`:

```make
lint:
    ruff check .

format:
    ruff format .
```

Or configure similar tasks via `nox`, `taskipy`, or `tox`.

---

## 🌍 Other Editors

* **PyCharm / JetBrains**: Set up Ruff as an external tool or run via terminal
* **NeoVim**: Use Ruff with `null-ls`, `efm-langserver`, or `conform.nvim`
* **Sublime Text**: Configure Ruff as a build system or integrate via plugin

---

That’s it! 🎉 You now have Ruff fully integrated into your Python dev workflow.

Want more? Check out the official docs:
👉 [https://docs.astral.sh/ruff](https://docs.astral.sh/ruff)


