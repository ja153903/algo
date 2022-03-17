from typing import List


class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        dups = set()
        j = 0

        for i in range(len(nums)):
            if nums[i] in dups:
                continue

            dups.add(nums[i])
            nums[j] = nums[i]
            j += 1

        return j
