from typing import List


class Solution:
    def canJump(self, nums: List[int]) -> bool:
        reach = 0
        i = 0

        while i < len(nums) and i <= reach:
            reach = max(reach, nums[i] + i)
            i += 1

        return i == len(nums)
