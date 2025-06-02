# 🧾 Common Poetry Commands

This reference summarizes the most useful Poetry commands for day-to-day development.

---

## 📦 Dependency Management

| Task                       | Command                                |
| -------------------------- | -------------------------------------- |
| Add a dependency           | `poetry add package_name`              |
| Add a dev dependency       | `poetry add --group dev package_name`  |
| Remove a dependency        | `poetry remove package_name`           |
| Update all dependencies    | `poetry update`                        |
| Update a specific package  | `poetry update package_name`           |
| Regenerate lockfile        | `poetry lock`                          |

---

## 📁 Project & Environment

| Task                              | Command                        |
| --------------------------------- | ------------------------------ |
| Create a new project              | `poetry new my_project`        |
| Initialize in an existing folder  | `poetry init`                  |
| Install dependencies              | `poetry install`               |
| Activate the virtual environment  | `poetry shell`                 |
| Run a command inside the venv     | `poetry run python script.py`  |
| Show venv path                    | `poetry env info --path`       |
| Remove the virtual environment    | `poetry env remove python`     |

---

## 🔐 Publishing

| Task                 | Command                                     |
| -------------------- | ------------------------------------------- |
| Build the package    | `poetry build`                              |
| Publish to PyPI      | `poetry publish --build`                    |
| Publish to TestPyPI  | `poetry publish --build -r test-pypi`       |
| Set PyPI token       | `poetry config pypi-token.pypi your_token`  |

---

## 🛠️ Miscellaneous

| Task                            | Command                                     |
| ------------------------------- | ------------------------------------------- |
| Show installed packages         | `poetry show`                               |
| Show dependency tree            | `poetry show --tree`                        |
| Set project version             | `poetry version 1.2.3`                      |
| Bump patch/minor/major version  | `poetry version patch` / `minor` / `major`  |
| Validate config & deps          | `poetry check`                              |

