"""
Given an integer array nums, return an array answer such that answer[i] is equal to the product of all the elements of nums except nums[i].

The product of any prefix or suffix of nums is guaranteed to fit in a 32-bit integer.

You must write an algorithm that runs in O(n) time and without using the division operation.

=== Solution ===

In this problem, we can do two linear scans. We can first go from left to right.
"""
from typing import List


class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # initialize result array to be 1
        result = [1] * len(nums)

        # first go from left to right
        for i in range(1, len(nums)):
            result[i] = result[i - 1] * nums[i - 1]

        # then go from right to left
        right = 1
        for i in range(len(nums) - 1, -1, -1):
            result[i] *= right
            right *= nums[i]

        return result
