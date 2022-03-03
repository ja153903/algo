"""
Given an integer array nums, find the contiguous subarray (containing at least one number) which has the largest sum and return its sum.

A subarray is a contiguous part of an array.

=== Solution ===
Typical solution here is to use Kadane's algorithm
"""
from typing import List


class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        max_so_far, current_max = nums[0], nums[0]

        for i in range(1, len(nums)):
            max_so_far = max(max_so_far + nums[i], nums[i])
            current_max = max(current_max, max_so_far)

        return current_max
