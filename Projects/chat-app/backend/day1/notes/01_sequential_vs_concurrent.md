# Notes: 01_sequential_vs_concurrent.py

**Date:** 2026-05-09

## Key concepts

- `asyncio.gather()` runs multiple coroutines concurrently — analogous to `Promise.all()` in JS
- Sequential `await` calls block one-at-a-time; total time = sum of all delays (~3s)
- Concurrent `gather()` runs all coroutines in the same event loop thread; total time = slowest single call (~1s)
- Return values come back in the same order as the arguments, regardless of which finishes first

## Gotchas / nuances

- `asyncio.gather()` still runs on a single thread — it's not parallelism, it's concurrency via cooperative multitasking
- All awaitables passed to `gather()` must be coroutines (or futures/tasks) — passing a plain function call won't work
- If one coroutine raises, `gather()` cancels the rest by default (unless `return_exceptions=True`)
