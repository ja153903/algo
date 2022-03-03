"""
Given an integer array nums, return all the triplets 
[nums[i], nums[j], nums[k]] such that i != j, i != k, and j != k, and nums[i] + nums[j] + nums[k] == 0.

Notice that the solution set must not contain duplicate triplets.

=== Solution ===

Given that we're going to need an algorithm that's going to take O(n^2),
we can take advantage of sorting here without performance degradation.

Once sorted, we should keep i fixed, and then use a two pointer solution for
j and k to figure out if there exists a solution such that nums[j] + nums[k] == -nums[i]
"""
from typing import List


class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        if not nums:
            return []

        n = len(nums)

        result = []

        nums.sort()

        for i in range(n - 2):
            if i == 0 or (i > 0 and nums[i] != nums[i - 1]):
                j, k = i + 1, n - 1

                while j < k:
                    current = nums[j] + nums[k]
                    target = -nums[i]

                    if current == target:
                        result.append([nums[idx] for idx in [i, j, k]])

                        while j < k and nums[j] == nums[j + 1]:
                            j += 1

                        while j < k and nums[k] == nums[k - 1]:
                            k -= 1

                        j += 1
                        k -= 1
                    elif current < target:
                        j += 1
                    else:
                        k -= 1

        return result
