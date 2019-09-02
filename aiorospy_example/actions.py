#!/usr/bin/env python3.7
import asyncio
import random

import aiorospy
import rospy
from actionlib.msg import TestAction, TestGoal, TestResult


class SimpleActionDemo:
    def __init__(self):
        self.server = aiorospy.AsyncActionServer('async_simple_action', TestAction, self.handle_action)
        self.client = aiorospy.AsyncActionClient('async_simple_action', TestAction)
        self.current_goal_handle = None

    async def handle_action(self, goal_handle):
        print('handle action')
        goal_id = goal_handle.get_goal_id().id.split('-')[1]
        old_goal_handle = self.current_goal_handle
        self.current_goal_handle = goal_handle
        try:
            if old_goal_handle:
                await asyncio.shield(self.server.cancel(old_goal_handle))

        except asyncio.CancelledError:
            print(f"Server: Interrupted before starting task {goal_id}")
            goal_handle.set_rejected()
            raise

        try:
            delay = goal_handle.get_goal().goal / 1000
            print(f"Server: Doing task {goal_id} for {delay}s")
            goal_handle.set_accepted()
            await asyncio.sleep(delay)
            goal_handle.set_succeeded()
            print(f"Server: Done task {goal_id}!")

        except asyncio.CancelledError:
            print(f"Server: Interrupted during task {goal_id}")
            goal_handle.set_canceled()
            raise

    async def exec_goal(self):
        number = random.randint(1, 1000)
        print(f"Client: Asking server to work for {number/1000}s")
        goal_handle = await self.client.ensure_goal(TestGoal(goal=number), resend_timeout=1.0)
        timeout=5
        try:
            await asyncio.wait_for(goal_handle.wait(), timeout=timeout)
        except asyncio.TimeoutError:
            print(f"Client: Giving up after {timeout}s...")
        print("---")


if __name__ == '__main__':
    rospy.init_node('simple_actions')

    loop = asyncio.get_event_loop()
    loop.set_debug(True)

    demo = SimpleActionDemo()

    tasks = asyncio.gather(
        demo.server.start(),
        demo.client.start(),
        demo.exec_goal()
    )

    aiorospy.cancel_on_exception(tasks)
    aiorospy.cancel_on_shutdown(tasks)

    try:
        loop.run_until_complete(tasks)
    except asyncio.CancelledError:
        pass
