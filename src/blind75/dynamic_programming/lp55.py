"""
You are given an integer array nums. 
You are initially positioned at the array's first index, 
and each element in the array represents your maximum jump length at that position.

Return true if you can reach the last index, or false otherwise.
"""
from typing import List


class Solution:
    def dp(self, nums: List[int]) -> bool:
        n = len(nums)
        dp = [False] * n

        dp[n - 1] = True

        for i in range(n - 2, -1, -1):
            j = 0

            while j <= nums[i] and i + j < n:
                if dp[i + j]:
                    dp[i] = True
                    break
                j += 1

        return dp[0]

    def canJump(self, nums: List[int]) -> bool:
        n = len(nums)
        reach = 0
        i = 0

        # i <= reach is our stopping condition here
        # because if we reach an index, but it's not possible
        # to ever reach that index from some previous index
        # then we break and possibly return false
        while i < n and i <= reach:
            reach = max(i + nums[i], reach)
            i += 1

        return i == n
