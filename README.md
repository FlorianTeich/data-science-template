# 🌱 data-science-template

## 🎁 Features

- organizational stuff
  - license
  - citation
  - contribution
  - code of conduct
  - changelog
  - security
- development quality of life
  - pre-commit
  - makefile
  - env file
  - dockerignore
  - gitignore
  - vscode settings
- good folder structure
- dependency management using uv
- linting
  - env
  - dockerfile
  - docker-compose
  - python
  - kubernetes-manifests
- formating
- type checking
- auditing dependencies
- inspecting dependencies
- creating sboms
- tests
  - unittests
  - coverage
  - mutationtesting
- docs
- CI/CD
  - Jenkinsfile
  - Dockerfile
  - docker-compose file

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
