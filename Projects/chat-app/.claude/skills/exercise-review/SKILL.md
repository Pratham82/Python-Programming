---
name: exercise-review
description: Validates exercise results. Use when the user wants to check their solution or confirm it works correctly. Triggers on "validate exercise", "check exercise", "exercise done", "did I do this right".
---

When reviewing an exercise:

1. Read the exercise file to understand what was asked (check the comments at the top for TASK and EXPECTED OUTPUT)
2. Run the exercise file using `uv run python <file>` from the backend directory
3. Compare actual output to the expected output in the comments

## Validation report

**Status:** Pass / Fail / Incomplete (TODOs remaining)

List what the solution got right, and flag anything missing or incorrect.

Keep the review concise — validate and done. To capture key concepts and gotchas, use the `take-notes` skill.