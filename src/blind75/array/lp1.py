"""
Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.

You may assume that each input would have exactly one solution, and you may not use the same element twice.

You can return the answer in any order.

=== Retrospective ===
The idea here is that if we want to solve this problem with a linear scan, then we would have to
store the indices we've seen before in a hashmap so that if we find a pair such that mp[j] + nums[i] == target
Or in this case if target - val is a key in the value (the complement), then we've found our answer
"""
from typing import List


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen = {}

        for i, val in enumerate(nums):
            if target - val in seen:
                return [seen[target - val], i]

            seen[val] = i

        return []
