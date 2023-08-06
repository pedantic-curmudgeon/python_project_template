"""Dev Container Python environment update content setup script."""


from pathlib import Path
from subprocess import run


def main() -> None:
    """Set up dev container's Python development environment."""
    repo_path = Path(__file__).resolve().parents[1]

    requirements_path = repo_path / "requirements.txt"
    run(f"pip install -r {requirements_path}", check=True, shell=True)

    dev_requirements_path = repo_path / "dev-requirements.txt"
    run(f"pip install -r {dev_requirements_path}", check=True, shell=True)
    run("pre-commit install", check=True, shell=True)


if __name__ == "__main__":
    main()
