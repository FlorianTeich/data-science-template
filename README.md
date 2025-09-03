# 🌱 data-science-template

## 🎁 Features

- Organizational Documentation
  - ⚖️ License
  - 🧾 Citation
  - 🤝 Contribution
  - 📜 Code of Conduct
  - 📝 Changelog
  - 🛡️ Security
- 🛠️ Development Quality of Life
  - 🪝 pre-commit
  - 🏗️ Makefile
  - 🧾 Env File
  - 🚫 .dockerignore
  - 🚫 .gitignore
  - ⚙️ VS Ccode Settings
- 📁 Good Folder Structure
- 📦 Dependency management using uv
- 🔍 linting
  - 🧾 Env
  - 🐋 Dockerfile
  - 🛳️ docker-compose
  - 🐍 Python
  - ☸️ Kubernetes Manifests
- ✨ Formating
- 📐 Type Checking
- 🔎 Auditing Dependencies
- 🧾 Inspecting Dependencies
- 🪪 Creating SBOMs
- 🧪 tests
  - 🧩 Unittests
  - 📊 Coverage
  - 🧬 Mutation Testing
- 📚 Documentation
- 🚀 CI/CD
  - 📝 Jenkinsfile
  - 🐳 Dockerfile
  - 🛳️ docker-compose file

## 🤲 Setup

> [!TIP]
> You should first [install uv](https://docs.astral.sh/uv/getting-started/installation/) to be able to run the commands below.

### Clone the repo

```
git clone https://github.com/FlorianTeich/data-science-template.git
```

### Install copier

```
uv tool install copier
```

### Create a new project

```
uvx copier copy data-science-template destination
```

### Installation of project

```
make install
```

## 🐘 Conventions to use

- Conventional Commit
- Semantic Versioning
- Google Style Docstrings
