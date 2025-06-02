# 📦 Dependency Management with Poetry

Poetry makes it easy to manage dependencies in a Python project. It handles both regular and development dependencies, pins versions in a lock file, and updates the `pyproject.toml` file automatically.

---

## ➕ Adding Dependencies

To add a regular dependency:

```bash
poetry add requests
```

This installs the latest compatible version and updates both `pyproject.toml` and `poetry.lock`.

To specify a version:

```bash
poetry add requests@^2.31
```

You can also use other version constraints:

* `==2.31.0` (exact version)
* `>=2.0,<3.0` (range)
* `~2.31.0` (compatible patch)
* `*` (any version — not recommended)

---

## ➕ Adding Development Dependencies

Use the `--group dev` flag to add a package needed only during development:

```bash
poetry add --group dev pytest
```

> Note: `--group dev` is the modern and recommended approach. The older `--dev` flag is still supported for backward compatibility.

This keeps test/linting tools separate from runtime packages.

---

## ➖ Removing Dependencies

To remove any dependency:

```bash
poetry remove requests
```

This will update both `pyproject.toml` and `poetry.lock`.

To remove a dev dependency:

```bash
poetry remove pytest
```

(There's no separate flag needed for dev dependencies.)

---

## ♻️ Updating Dependencies

To update a specific package:

```bash
poetry update requests
```

To update all dependencies:

```bash
poetry update
```

This refreshes versions based on the constraints defined in `pyproject.toml`.

---

## 📋 Listing Dependencies

To list all installed packages:

```bash
poetry show
```

To show a tree of installed packages with their dependencies:

```bash
poetry show --tree
```

---

## 🔍 Checking for Package Info

To see details about a package:

```bash
poetry show requests
```

You’ll get version, description, dependencies, and more.

---

## 🧪 Using Extras

Some packages have optional “extras” (like `requests[socks]`):

```bash
poetry add "requests[socks]"
```

---

## 🛠️ Using Path, Git, or URL Dependencies

### Local path:

```bash
poetry add ../my_local_package
```

### Git repository:

```bash
poetry add git+https://github.com/user/repo.git
```

You can also specify a branch, tag, or commit:

```bash
poetry add "git+https://github.com/user/repo.git#main"
```

---

## 🔐 The `poetry.lock` File

Poetry automatically generates `poetry.lock` to ensure consistent installs across environments.

* Don’t edit this file manually.
* Commit it to version control for reproducibility.

---

## 📘 Related Topics

* [Understanding `pyproject.toml`](03_pyproject_toml.md)
* [Virtual Environment Handling](05_virtualenv_handling.md)

