from typing import List


class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        def backtrack(nums, result, current):
            if len(current) == len(nums):
                result.append(list(current))
            else:
                for i in range(len(nums)):
                    if nums[i] in current:
                        continue
                    current.append(nums[i])
                    backtrack(nums, result, current)
                    current.pop()

        result = []
        current = []

        backtrack(nums, result, current)

        return result
