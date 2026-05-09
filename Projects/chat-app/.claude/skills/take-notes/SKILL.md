---
name: take-notes
description: Captures key concepts and gotchas from an exercise into a notes file. Use when the user wants to document what they learned, save key concepts, or record gotchas from an exercise. Triggers on "take notes", "save notes", "document learnings", "note this down", "save what I learned".
---

When taking notes for an exercise:

1. If the user hasn't specified a file, ask which exercise file these notes are for — or infer it from the current conversation context.
2. Read the exercise file to understand what it covers.
3. Extract the following from the exercise and conversation context:

## Note structure

Create a file at `notes/<exercise-filename>.md` (same name as the exercise file, `.md` extension) relative to the exercise file's directory.

Use this template:

```markdown
# Notes: <exercise filename>

**Date:** <today's date>

## Key concepts

- <2–4 bullet points of what this exercise teaches — the "why" behind what was built>
- Draw analogies to JS/other languages when relevant (e.g. `asyncio.gather()` = `Promise.all()`)

## Gotchas / nuances

- <Subtle behavior revealed by the exercise that could trip someone up later>
```

4. Create the `notes/` folder next to the exercise file if it doesn't exist.
5. Write the file using the Write tool.
6. Confirm the file was created and show the path.

Keep notes concise — bullet points only, no prose paragraphs.
