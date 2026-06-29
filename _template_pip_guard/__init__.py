import sys
from typing import Never

_MESSAGE = """\
Do not use pip in this template.

This project is managed by uv. Installing packages with pip will not update
pyproject.toml or uv.lock, so the dependency can disappear after the next
uv sync.

Use one of these commands instead:
  uv add <package>
  uv add --dev <package>
  uv sync --group dev

If you only need a pip-compatible interface for an advanced one-off case, use:
  uv pip <command>
"""


def main() -> Never:
    sys.stderr.write(_MESSAGE)
    raise SystemExit(2)
