# DAY 1 — EXERCISE 3: Tasks and Cancellation
#
# TASK: In your chat app, each connected user has a background "heartbeat" loop
# that sends a ping every second to keep the connection alive.
# When a user disconnects, that loop must be cancelled cleanly.
#
# STEPS:
#   1. Implement heartbeat() — prints "[user_id] ping #N" every second, forever
#      Handle CancelledError by printing "[user_id] disconnected cleanly"
#      and re-raising it (important!)
#   2. In main():
#      a. Start heartbeat tasks for user 1 and user 2 using asyncio.create_task()
#      b. Wait 3 seconds
#      c. Disconnect user 1 (cancel their task, await it inside try/except)
#      d. Wait 2 more seconds
#      e. Disconnect user 2
#   3. Run: $ uv run python day1/03_tasks_and_cancellation.py
#
# EXPECTED OUTPUT:
#   [user_1] ping #1
#   [user_2] ping #1
#   [user_1] ping #2
#   ...
#   Disconnecting user 1...
#   [user_1] disconnected cleanly
#   [user_2] ping #4
#   ...

import asyncio


async def heartbeat(user_id: str):
    # TODO:
    # 1. count = 0, loop forever
    # 2. increment count, print f"[{user_id}] ping #{count}"
    # 3. await asyncio.sleep(1)
    # 4. wrap the loop in try/except asyncio.CancelledError
    #    print clean disconnect message and re-raise
    pass


async def main():
    # TODO:
    # 1. Create tasks for user_1 and user_2 using asyncio.create_task()
    # 2. await asyncio.sleep(3)
    # 3. print "Disconnecting user 1..."
    # 4. Cancel task_1, await it in try/except CancelledError
    # 5. await asyncio.sleep(2)
    # 6. print "Disconnecting user 2..."
    # 7. Cancel task_2, await it in try/except CancelledError
    # 8. print "All users disconnected."
    pass


asyncio.run(main())
