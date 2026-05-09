# DAY 1 — EXERCISE 4: Timeouts
#
# TASK: Your chat app saves messages to a database. If the DB is slow or
# unresponsive, you don't want to hang forever — you want to timeout and
# return an error to the user quickly.
#
# STEPS:
#   1. Implement save_message() — simulates a DB write that takes `delay` seconds
#   2. Implement save_with_timeout():
#      - try to save the message with a 2s timeout using asyncio.wait_for()
#      - if it succeeds, print "message saved"
#      - if it times out, print "DB timeout — message not saved"
#   3. Call save_with_timeout() twice in main():
#      - once with a fast DB (delay=0.5s) → should succeed
#      - once with a slow DB (delay=4s) → should timeout
#   4. Run: $ uv run python day1/04_timeouts.py
#
# EXPECTED OUTPUT:
#   Saving message (fast DB)...
#   message saved
#   Saving message (slow DB)...
#   DB timeout — message not saved

import asyncio


async def save_message(content: str, delay: float) -> str:
    # TODO: simulate DB write — sleep for `delay` seconds, then return "saved"
    pass


async def save_with_timeout(content: str, delay: float):
    print(f"Saving message (delay={delay}s)...")
    # TODO:
    # try:
    #     result = await asyncio.wait_for(save_message(...), timeout=2.0)
    #     print(...)
    # except asyncio.TimeoutError:
    #     print(...)
    pass


async def main():
    await save_with_timeout("hello world", delay=0.5)
    print()
    await save_with_timeout("hello world", delay=4.0)


asyncio.run(main())
