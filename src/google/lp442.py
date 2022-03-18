from typing import List


class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        """
        The logic with this approach relies on marking a number as negative
        if we haven't seen it before, but if its a problem we've seen before i.e. it's already negative, we append it to the result
        """
        result = []

        for num in nums:
            if nums[abs(num) - 1] < 0:
                result.append(abs(num))
            else:
                nums[abs(num) - 1] *= -1

        return result
