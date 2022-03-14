from typing import List


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        last_seen = {}

        for i, val in enumerate(nums):
            if target - val in last_seen:
                return [last_seen[target - val], i]

            last_seen[val] = i

        return []
