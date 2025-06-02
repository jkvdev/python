# 🚀 Publishing Packages with Poetry

Poetry makes it easy to build and publish Python packages to [PyPI](https://pypi.org/) or private registries. It handles everything from metadata to versioning to uploading — all from the command line.

---

## 📦 Build a Package

To build your package (generating `.tar.gz` and `.whl` files):

```bash
poetry build
```

This creates a `dist/` folder with the build artifacts:

```bash
dist/
├── my_project-0.1.0.tar.gz
└── my_project-0.1.0-py3-none-any.whl
```

Ensure your `pyproject.toml` includes correct metadata, like:

```toml
[tool.poetry]
name = "my_project"
version = "0.1.0"
description = "A sample package"
authors = ["Your Name <you@example.com>"]
readme = "README.md"
license = "MIT"
homepage = "https://github.com/yourusername/my_project"
repository = "https://github.com/yourusername/my_project"
```

---

## 🔑 Authentication with PyPI

To publish, you'll need a valid PyPI account.

### Configure Credentials (First Time)

Use Poetry to set your API token securely:

```bash
poetry config pypi-token.pypi your_token_here
```

> You can generate your token at: [https://pypi.org/account/token/](https://pypi.org/account/token/)
> Keep your tokens private and avoid committing them to version control.

---

## ☁️ Publish to PyPI

Once built and configured, publish with:

```bash
poetry publish --build
```

This automatically builds the package (if needed) and uploads it to PyPI.
Make sure the version you're publishing does not already exist on PyPI, or the upload will fail.

---

## 🧪 Test First with TestPyPI

To avoid affecting real packages, test your release using [TestPyPI](https://test.pypi.org/):

```bash
poetry config repositories.test-pypi https://test.pypi.org/legacy/
poetry publish --build -r test-pypi
```

If you're using a token for TestPyPI:

```bash
poetry config pypi-token.test-pypi your_test_token_here
```

---

## 🔁 Bumping Versions

To change your version (according to [semantic versioning](https://semver.org/)):

```bash
poetry version patch    # 0.1.0 → 0.1.1
poetry version minor    # 0.1.0 → 0.2.0
poetry version major    # 0.1.0 → 1.0.0
```

You can also set it manually:

```bash
poetry version 1.2.3
```

This updates the version in `pyproject.toml`.

---

## 📘 Related Topics

* [Understanding `pyproject.toml`](03_pyproject_toml.md)
* [Virtual Environment Handling](05_virtualenv_handling.md)

