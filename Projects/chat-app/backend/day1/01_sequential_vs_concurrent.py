# DAY 1 — EXERCISE 1: Sequential vs Concurrent
#
# TASK: You're building a chat app that needs to load a user's profile.
# Loading involves 3 independent steps:
#   - fetch the user record
#   - fetch their recent messages
#   - fetch their contacts list
#
# Right now it's done sequentially (slow). Your job:
#   1. Run this file as-is and note how long it takes
#   2. Write a concurrent version using asyncio.gather()
#   3. Run again and compare the time
#
# STEPS:
#   $ uv run python day1/01_sequential_vs_concurrent.py

import asyncio
import time


async def fetch_user_record(user_id: int) -> dict:
    await asyncio.sleep(1)  # simulates DB query
    return {"id": user_id, "name": "Alice"}


async def fetch_recent_messages(user_id: int) -> list:
    await asyncio.sleep(1)  # simulates DB query
    return ["msg1", "msg2", "msg3"]


async def fetch_contacts(user_id: int) -> list:
    await asyncio.sleep(1)  # simulates DB query
    return ["Bob", "Charlie"]


# --- Part A: Sequential (already done — just run it) ---

async def load_profile_sequential(user_id: int):
    start = time.perf_counter()

    user = await fetch_user_record(user_id)
    messages = await fetch_recent_messages(user_id)
    contacts = await fetch_contacts(user_id)

    elapsed = time.perf_counter() - start
    print(f"[sequential] loaded in {elapsed:.2f}s")
    print(f"  user={user}, messages={messages}, contacts={contacts}")


# --- Part B: YOUR TASK — write the concurrent version ---
# Use asyncio.gather() to run all 3 fetches at the same time.
# Expected time: ~1s instead of ~3s

async def load_profile_concurrent(user_id: int):
    start = time.perf_counter()

    # TODO: use asyncio.gather() to fetch all 3 concurrently
    # user, messages, contacts = await asyncio.gather(...)
    user, messages, contacts = await asyncio.gather(fetch_user_record(user_id), fetch_recent_messages(user_id), fetch_contacts(user_id))

    elapsed = time.perf_counter() - start
    # TODO: uncomment when done
    print(f"[concurrent] loaded in {elapsed:.2f}s")
    print(f"  user={user}, messages={messages}, contacts={contacts}")


async def main():
    print("=== Sequential ===")
    await load_profile_sequential(user_id=1)

    print("\n=== Concurrent ===")
    await load_profile_concurrent(user_id=1)


asyncio.run(main())
