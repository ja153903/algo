"""
You are a professional robber planning to rob houses along a street. 
Each house has a certain amount of money stashed, the only constraint
stopping you from robbing each of them is that adjacent houses have security 
systems connected and it will automatically contact the police if two adjacent
houses were broken into on the same night.

Given an integer array nums representing the amount of money of each house, 
return the maximum amount of money you can rob tonight without alerting the police.

=== Solution ===

O(n) space and O(n) time

dp[i] ~ max amount up to house i
dp[0] = nums[0]
dp[1] = max(nums[0], nums[1])

dp[i] = max(dp[i - 1], dp[i - 2] + nums[i])

We can probably optimize here for space
"""
from typing import List


class Solution:
    def rob(self, nums: List[int]) -> int:
        if not nums:
            return 0

        if len(nums) == 1:
            return nums[0]

        if len(nums) == 2:
            return max(nums)

        dp = [0] * len(nums)
        dp[0] = nums[0]
        dp[1] = max(nums[:2])

        for i in range(2, len(nums)):
            dp[i] = max(dp[i - 1], dp[i - 2] + nums[i])

        return dp[-1]

    def space_optimization(self, nums: List[int]) -> int:
        if not nums:
            return 0

        p1, p2 = 0, 0

        for num in nums:
            p1, p2 = max(p2 + num, p1), p1

        return p1
