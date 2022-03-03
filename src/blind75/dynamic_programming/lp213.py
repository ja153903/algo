"""
This is House Robber but houses are in a circle.

=== Solution ===
Because the houses are in a circular, what we can do here
is we can omit one value from the front
and then do another case where we omit one value from the end.
"""
from typing import List


class Solution:
    def rob(self, nums: List[int]) -> int:
        if not nums:
            return 0

        if len(nums) == 1:
            return nums[0]

        return max(self.logic(nums[1:]), self.logic(nums[:-1]))

    def logic(self, nums: List[int]) -> int:
        if not nums:
            return 0

        p1, p2 = 0, 0

        for num in nums:
            p1, p2 = max(p2 + num, p1), p1

        return p1
