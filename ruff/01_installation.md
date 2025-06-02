# 📦 Installation

Ruff can be installed in several ways depending on your system and preference. The most common method is via `pip`, but it's also available through `brew` (on macOS) or by compiling from source with `cargo`.

---

## ✅ Install with pip

This is the recommended and most portable way:

```bash
pip install ruff
```

To upgrade:

```bash
pip install --upgrade ruff
```

You can also add it to your project dependencies (e.g. in `pyproject.toml`, `requirements.txt`, or `poetry`).

---

## 🍺 Install with Homebrew (macOS)

If you're on macOS and use [Homebrew](https://brew.sh):

```bash
brew install ruff
```

---

## 🛠️ Install via Cargo (Rust)

If you have Rust installed:

```bash
cargo install ruff
```

Note: This installs Ruff from source, which may take slightly longer to compile but results in the same fast performance.

---

## 🧪 Verify the Installation

After installation, check that it's working:

```bash
ruff --version
```

*Example output:*

```
ruff 0.4.3
```

---

You're now ready to start using Ruff! Head over to [`02_basic_usage.md`](02_basic_usage.md) to learn how to run it. 🚀

