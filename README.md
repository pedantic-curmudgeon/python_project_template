# python_project_template

A Python project template.

## Includes

1. [A Dev Container with Python 3.11 and Docker-In-Docker.](.devcontainer/devcontainer.json)
1. [Visual Studio Code code quality extensions and configurations.](.devcontainer/devcontainer.json#L14-L58)
1. [Pre-commit code quality configurations.](.pre-commit-config.yaml)
1. [Dependabot configurations to update requirements.](.github/dependabot.yml)
1. [A GitHub workflow which runs pre-commit.](.github/workflows/pre_commit.yml)
1. [A GitHub workflow which runs pytest.](.github/workflows/pytest.yml)
1. [A GitHub workflow which runs pre-commit and pytest on pull requests.](.github/workflows/pr.yml)

## Requirements

1. [VS Code](https://code.visualstudio.com/)
1. [Dev Containers Extension](https://marketplace.visualstudio.com/items?itemName=ms-vscode-remote.remote-containers)
1. [Docker](https://www.docker.com/)

*Required for use outside of GitHub Codespaces.*

## Running Tests

### GitHub

Open a pull request.

### Local Environment

Execute the following commands:

```shell
python tests/run_pytest.py
```

*This will create `htmlcov/`, `coverage.xml`, and `results.xml` in the `tests/` folder.*

## Troubleshooting

If a VS Code extension is not working, open the Command Palette and run the Developer:
Reload Window command to refresh VS Code.
