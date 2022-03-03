"""
Given an integer array nums, return the length of the longest strictly increasing subsequence.

A subsequence is a sequence that can be derived from an array by deleting some or no elements 
without changing the order of the remaining elements. 

For example, [3,6,2,7] is a subsequence of the array [0,3,1,6,2,2,7].

=== Solution ===

Recursively, we solve this solution by enumerating every possible LIS.

Given some starting index, we keep track of the following: LIS(arr, idx, prev, count, max)

=== Solution ===
What is the recursive solution here?

For each starting index, we want to enumerate all possible paths, keeping track of the maximum lengths we've found so far via
some global variable.

This run time is O(2^n) so we can improve this with an algorithm that runs in O(n^2).

The DP algorithm here has the following state: dp[i] ~ denotes the maximum length of an increasing subsequence
up to and including index i.

All values should be initialized to 1 because the shortest possible increasing subsequence is 1 if the length of the array
is at least 1. Otherwise, we have an edge case of 0 when the array is empty.

So then our update step requires us to look back on all indices from [0, i) checking if nums[i] > nums[j] for j in [0, i).
If the current number at index i is in fact greater than some past number at index j.
Then we should update dp[i] = max(dp[i], dp[j] + 1) for j in [0, i)

We then update our global max if necessary
"""
from typing import List


class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        if not nums:
            return 0
       
        dp = [1] * len(nums)
        max_len = 1

        for i in range(1, len(nums)):
            for j in range(0, i):
                if nums[i] > nums[j]:
                    dp[i] = max(dp[i], dp[j] + 1)
            max_len = max(max_len, dp[i])

        return max_len
