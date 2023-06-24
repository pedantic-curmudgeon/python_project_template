# python_project_template

A Python project template.

## Includes

1. A Dev Container.
2. Visual Studio Code code quality extensions and configurations.
3. Pre-commit code quality configurations.
4. Dependabot configurations to update requirements.
5. A GitHub workflow which runs pre-commit on pull requests.

## Known Issues

1. All VS Code extensions may not be fully-operational after the Dev Container is built.
This is related to race conditions when installing extensions in VS Code. There are
several related issues open with Microsoft. To work around this issue, after the Dev
Container is built, open the Command Palette and run the Developer: Reload Window
command to refresh VS Code.
