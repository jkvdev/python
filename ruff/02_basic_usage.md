# 🚀 Basic Usage

Once Ruff is installed, you can start linting and formatting your Python code directly from the command line.

---

## 🔍 Linting Code

To check an entire project or directory:

```bash
ruff check .
```

You can also check a specific file:

```bash
ruff check app/main.py
```

---

## 🛠️ Auto-Fix Issues

Ruff can automatically fix many issues it detects:

```bash
ruff check . --fix
```

You can combine multiple flags:

```bash
ruff check src/ --fix --show-fixes
```

---

## 🎨 Formatting Code

Ruff can format your code, similar to tools like `black`:

```bash
ruff format .
```

Format a specific file:

```bash
ruff format app/models.py
```

---

## 📂 Common Options

Here are some common options you can pass to `ruff check`:

| Flag            | Description                     |
| --------------- | ------------------------------- |
| `--fix`         | Automatically fix lint issues   |
| `--show-fixes`  | Show which rules were fixed     |
| `--select`      | Run only specific rule codes    |
| `--ignore`      | Skip specific rule codes        |
| `--exclude`     | Skip certain files/directories  |

Example: only check for unused imports (F401):

```bash
ruff check . --select F401
```

---

## 🧾 Sample Rule Codes

Ruff uses short rule codes, especially from the `F` category (based on `pyflakes`):

| Code   | Description                         |
| ------ | ----------------------------------- |
| F401   | Unused import                       |
| F841   | Local variable assigned but unused  |
| F821   | Undefined name                      |
| F632   | Use of `==` / `!=` with `None`      |

You can combine rules too:

```bash
ruff check . --select F401,F841
```

For the full list of rules, see the [Ruff rule reference](https://docs.astral.sh/ruff/rules/).

---

Now that you know how to run Ruff from the command line, check out [`03_configuration.md`](03_configuration.md) to learn how to customize its behavior. ⚙️

