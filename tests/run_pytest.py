"""Run pytest."""

import sys
from pathlib import Path
from subprocess import run


def run_pytest() -> int:
    """Run pytest."""
    tests_folder = Path(__file__).resolve().parent
    repo_folder = tests_folder.parent

    return run(
        args=(
            "pytest",
            tests_folder,
            "--numprocesses=auto",
            "--durations=0",
            "--verbosity=2",
            f"--junitxml={tests_folder}/results/results.xml",
            f"--cov={repo_folder}",
            f"--cov-config={tests_folder}/.coveragerc",
            f"--cov-report=html:{tests_folder}/results/htmlcov",
            "--cov-report=term",
            f"--cov-report=xml:{tests_folder}/results/coverage.xml",
        ),
        check=False,
    ).returncode


if __name__ == "__main__":
    sys.exit(run_pytest())
