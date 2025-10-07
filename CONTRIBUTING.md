# Contributing Guidelines

Thank you for your interest in contributing!

## 🧭 Workflow

1. **Never commit directly to `main`**.  
   Always create a dedicated branch for each new feature, fix, or documentation update.  

2. **Branch naming convention**
    Use descriptive branch names:
    - feat/<short-feature-name> for new features
    - fix/<short-description> for bug fixes
    - docs/<update-name> for documentation
    - chore/<config-or-maintenance> for configuration or maintenance
    - test/<scope> → add or modify tests

3. **Pull Requests**
    - Open a PR from your feature branch to `main`
    - Add a clear title and short description of what’s changed
    - Use the PR as a self-review tool: check diffs, comments, and formatting
    - Use **“Squash and merge”** when merging to keep a clean history
    - Delete the feature branch after merging

## 🧱 Commit Messages

Follow the [Conventional Commits](https://www.conventionalcommits.org/en/v1.0.0/) style:

| Type | Description |
|------|--------------|
| `feat:` | New feature |
| `fix:` | Bug fix |
| `docs:` | Documentation changes |
| `chore:` | Maintenance, setup, dependencies |
| `test:` | Add or update tests |
| `refactor:` | Code improvement without behavior change |


## 🧪 Testing (future)

When the testing suite is added:
- Run all tests before opening a PR
- Include new test cases for each new feature or bug fix

## 🧾 Code Style

- Follow PEP8 guidelines for Python code
- Keep functions and classes small and focused
- Write descriptive names and clear docstrings
- Avoid committing commented-out or debug code


