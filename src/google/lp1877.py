from typing import List


class Solution:
    def minPairSum(self, nums: List[int]) -> int:
        nums.sort()

        maxpair = nums[0] + nums[-1]

        i, j = 1, len(nums) - 2

        while i < j:
            maxpair = max(maxpair, nums[i] + nums[j])
            i += 1
            j -= 1

        return maxpair
