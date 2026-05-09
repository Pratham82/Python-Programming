# DAY 1 — EXERCISE 2: Fake API Fetch
#
# TASK: Simulate sending a message to multiple users at once.
# Your chat app needs to notify 4 users that they have a new message.
# Each notification call takes a random amount of time.
#
# STEPS:
#   1. Implement notify_user() — it should print "notifying user X..." wait
#      a random 0.5–2s delay, then print "user X notified"
#   2. Implement notify_all() — notify all 4 users concurrently using gather()
#   3. Print total time taken at the end
#   4. Run: $ uv run python day1/02_fake_api_fetch.py
#
# EXPECTED OUTPUT (order will vary due to random delays):
#   Notifying 4 users...
#   notifying user 3...
#   notifying user 1...
#   ...
#   user 2 notified
#   user 4 notified
#   All notified in ~1.8s   ← roughly the slowest single call, not sum of all

import asyncio
import random
import time


async def notify_user(user_id: int) -> str:
    # TODO:
    # 1. print "notifying user {user_id}..."
    # 2. wait a random delay between 0.5 and 2.0 seconds (use random.uniform)
    # 3. print "user {user_id} notified"
    # 4. return f"ok:{user_id}"
    pass


async def notify_all(user_ids: list[int]):
    start = time.perf_counter()
    print(f"Notifying {len(user_ids)} users...\n")

    # TODO: run notify_user() for all user_ids concurrently using asyncio.gather()
    # results = await asyncio.gather(...)

    elapsed = time.perf_counter() - start
    # TODO: print total time and results


asyncio.run(notify_all([1, 2, 3, 4]))
