"""Dev container Python environment post create setup script."""

from pathlib import Path
from subprocess import run


def main() -> None:
    """Set up dev container's Python development environment."""
    repo_path = Path(__file__).resolve().parents[1]

    # Install requirements.
    requirements_path = repo_path / "requirements.txt"
    if requirements_path.exists():
        run(f"pip install -r {requirements_path}", check=True, shell=True)


if __name__ == "__main__":
    main()
