"""
Given an integer array nums, return true if any value appears at least twice in the array, and return false if every element is distinct.

=== Solution ===

One solution is to iterate over the entire array keeping track of unique integers in a set.
If we encounter a number that already exists in the set, then we know there's a duplicate so we return True.
Otherwise if there were no duplicates after iteration, we return False
"""
from typing import List


class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        seen = set()

        for num in nums:
            if num in seen:
                return True

            seen.add(num)

        return False
