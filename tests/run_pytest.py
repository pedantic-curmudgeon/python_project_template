"""Run pytest."""

import sys
from pathlib import Path
from subprocess import run


def run_pytest() -> int:
    """Run pytest."""
    tests_folder = Path(__file__).resolve().parent
    test_results_path = tests_folder / "pytest_results.xml"

    return run(
        args=(
            "pytest",
            "--verbose",
            tests_folder,
            f"--junitxml={test_results_path}",
        ),
        check=False,
    ).returncode


if __name__ == "__main__":
    sys.exit(run_pytest())
