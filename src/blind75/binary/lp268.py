"""
Given an array nums containing n distinct numbers in the range [0, n],
return the only number in the range that is missing from the array.

=== Solution ===
We can use bit manipulation to solve this problem.

The idea with this solution is that the XOR operation is commutative.

There are also n + 1 possible numbers that we choose from.

We then should accumulate the XOR of all possible values in the array.

The reason this works is because i ^ i = 0.

So if we compare i ^ nums[i] while iterating over all possible indices
and numbers, then at the end we'll find the missing value.
"""
from typing import List


class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        xor, i = 0, 0

        while i < len(nums):
            xor = xor ^ i ^ nums[i]
            i += 1

        return xor ^ i
