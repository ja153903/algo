from typing import List


class Solution:
    def findMissingRanges(self, nums: List[int], lower: int, upper: int) -> List[str]:
        """
        Idea is to collect first and last integers between nums
        So for example if lower = -5, upper= 10, and nums = [1, 3, 5, 7]
        Then we have the following ranges:
        [-5, 0], [2], [4], [6], [8, 10]

        There are three cases to consider.
        * if lower is less than first number in nums
        * numbers in between each other in nums
        * if upper is greater than last number in nums
        """
        if not nums:
            if lower == upper:
                return [str(lower)]
            else:
                return [f"{lower}->{upper}"]

        result = []

        # If lower is less than first number in nums
        if lower < nums[0]:
            if lower == nums[0] - 1:
                result.append(str(lower))
            else:
                result.append(f"{lower}->{nums[0] - 1}")

        # between each other in nums
        for i in range(1, len(nums)):
            if nums[i] - nums[i - 1] == 1:
                continue
            elif nums[i] - nums[i - 1] == 2:
                result.append(str(nums[i] - 1))
            else:
                result.append(f"{nums[i - 1] + 1}->{nums[i] - 1}")

        if nums[-1] < upper:
            if nums[-1] + 1 == upper:
                result.append(str(upper))
            else:
                result.append(f"{nums[-1] + 1}->{upper}")

        return result
