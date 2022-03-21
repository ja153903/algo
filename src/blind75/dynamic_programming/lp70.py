"""
You are climbing a staircase. It takes n steps to reach the top.

Each time you can either climb 1 or 2 steps. In how many distinct ways can you climb to the top?

=== Solution ===

This problem is a Fibonacci problem.
"""


class Solution:
    def climbStairs(self, n: int) -> int:
        a, b = 1, 1

        for _ in range(n):
            a, b = b, a + b

        return a
