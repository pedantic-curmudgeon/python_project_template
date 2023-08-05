"""Run pytest."""

import sys
from pathlib import Path
from subprocess import run


def run_pytest() -> int:
    """Run pytest."""
    return run(
        args=(
            "pytest",
            Path(__file__).resolve().parent,
            "--numprocesses=auto",
            "--durations=0",
            "--verbosity=2",
            "--junitxml=results.xml",
            "--cov=../",
            "--cov-report=term",
            "--cov-report=html",
            "--cov-report=xml",
        ),
        check=False,
    ).returncode


if __name__ == "__main__":
    sys.exit(run_pytest())
