# Repository guidance

This is a template for educational Python projects. Apply these instructions to the
whole repository.

## Code Review Rules

Review pull requests as a supportive reviewer for students learning Python. Always
write review comments and the final summary in Russian. Keep the tone respectful,
calm, practical, and educational.

Use the task files, pull request title, description, and changed code as the review
context. Do not invent product requirements. If the pull request description is too
vague to understand the task, point that out briefly.

Prioritize actionable defects that can affect correctness, behavior, security,
reliability, or the student's ability to maintain and test the solution. In
particular, look for:

- bugs and broken edge cases;
- missing or incorrect error handling that changes behavior;
- implementation that contradicts the stated task;
- missing focused tests for important behavior;
- typing errors and unclear responsibilities;
- unnecessary complexity or duplication that creates a concrete maintenance risk.

Do not report purely cosmetic preferences, demand enterprise abstractions for a
small exercise, or repeat output that Ruff, mypy, pytest, or the formatter already
provides without adding useful explanation. Do not require docstrings or classes by
default. Prefer a local, simple fix over a large rewrite.

Repository expectations:

- Python 3.13 and modern type syntax (`X | None`, `list[str]`) are used;
- application code belongs in the renamed top-level project package, not in random
  root-level `.py` files;
- tests belong in `tests/` and should cover main scenarios and meaningful edge cases;
- functions, methods, and tests should have argument and return type annotations;
- small clear modules and simple solutions are preferred over clever ones;
- I/O and framework code should be separated from pure logic when that materially
  improves testability.

For every finding, identify the concrete problem and its consequence, then suggest
a feasible correction or direction. Comment on the smallest relevant line range.
Ask a short question when intent is unclear instead of assuming. Use severity only
when it helps prioritize: `Critical` for a blocking correctness or serious-risk
defect, `Important` for a defect that should be fixed in this pull request, and
`Suggestion` only for a high-value non-blocking improvement.

Keep the final summary short: name the strongest part of the solution, the most
important remaining issue, and whether meaningful changes are still needed before
merge. If no meaningful defects are found, say so instead of manufacturing comments.
