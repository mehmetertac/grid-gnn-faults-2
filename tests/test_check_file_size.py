"""Smoke test for the 1,000-line guardrail script."""

from __future__ import annotations

import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


def test_check_file_size_passes_on_repo():
    result = subprocess.run(
        [sys.executable, str(ROOT / "scripts" / "check_file_size.py")],
        cwd=ROOT,
        capture_output=True,
        text=True,
        check=False,
    )
    assert result.returncode == 0, result.stdout + result.stderr
