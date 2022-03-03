"""
Given an integer array nums, find a contiguous non-empty subarray within the array that has the largest product, and return the product.

The test cases are generated so that the answer will fit in a 32-bit integer.

A subarray is a contiguous subsequence of the array.

=== Solution ===
The solution we created with Kadane's algorithm can be extended to solve this problem as well.
However, the difference here is that we need to take into account the minimum value.
"""
from typing import List


class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        max_so_far, min_so_far, current_max = nums[0], nums[0], nums[0]

        for i in range(1, len(nums)):
            min_so_far, max_so_far = min(
                min_so_far * nums[i], max_so_far * nums[i], nums[i]
            ), max(min_so_far * nums[i], max_so_far * nums[i], nums[i])

            current_max = max(current_max, max_so_far)

        return current_max
