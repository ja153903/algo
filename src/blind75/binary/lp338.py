"""
Given an integer n, return an array ans of length n + 1 such that for each i (0 <= i <= n), 
ans[i] is the number of 1's in the binary representation of i.

=== Solution ===

For this problem, we want to go beyond the solution that we can create in O(n log n) time.

To do that, we should use dynamic programming here, but we should find what the proper
pattern is to use.

Let's go through a test:

0 -> 0
1 -> 1
2 -> 10
3 -> 11
4 -> 100
5 -> 101

dp[0] = 0
dp[1] = 1
dp[2] = 1
dp[3] = 2
dp[4] = 1
dp[5] = 2

Let's set dp[0] = 0 to be our base case.
For each number from 0 to n, we can then see that
dp[i] = dp[i >> 1] + (i & 1)

Note that we increase by 1 if the right most bit is a 1 which is why we check (i & 1)

i >> 1 => this does a right shift of 1 bit so for example, 2 >> 1 => 01

This means that dp[2] = dp[1] + (i & 1)

For a large example like dp[3], 3 >> 1 => 01
so dp[3] = dp[1] + (3 & 1) = 2
"""
from typing import List


class Solution:
    def countBits(self, n: int) -> List[int]:
        dp = [0] * (n + 1)

        for i in range(1, n + 1):
            dp[i] = dp[i >> 1] + (i & 1)

        return dp
