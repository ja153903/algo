"""
Given an array of distinct integers nums and a target integer target,
return the number of possible combinations that add up to target.

The test cases are generated so that the answer can fit in a 32-bit integer.

=== Solution ===
The idea with this solution is to keep track in our memoization array
the number of possible permutations to come up to some target value i
so generally dp[i] ~ the number of possible permutations to get i

dp[0] = 1 is the base case where there is 1 way to get 0.
This statement is only true because we do not take into account negative numbers.

generally, dp[i] = sum of dp[i - num] for num in nums if num >= 0
"""
from typing import List


class Solution:
    def combinationSum4(self, nums: List[int], target: int) -> int:
        dp = [0] * (target + 1)

        dp[0] = 1

        for i in range(1, target + 1):
            for num in nums:
                if i - num >= 0:
                    dp[i] += dp[i - num]

        return dp[target]
