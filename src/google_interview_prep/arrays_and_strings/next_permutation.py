from typing import List


"""
Given some initial sequence,

1. Find longest non-increasing suffix
2. Identify pivot which is the left of the start of the non-increasing suffix
3. Find rightmost successor to pivot in the suffix
4. Swap the pivot
5. Reverse the suffix
"""


class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        pivot = self.get_pivot_index(nums) - 1
        if pivot != -1:
            rightmost_successor = self.get_rightmost_successor(nums, nums[pivot])
            nums[pivot], nums[rightmost_successor] = (
                nums[rightmost_successor],
                nums[pivot],
            )

        i, j = pivot + 1, len(nums) - 1

        while i < j:
            nums[i], nums[j] = nums[j], nums[i]
            i += 1
            j -= 1

    def get_pivot_index(self, nums: List[int]) -> int:
        for i in range(len(nums) - 1, 0, -1):
            if nums[i] > nums[i - 1]:
                return i

        return 0

    def get_rightmost_successor(self, nums: List[int], threshold: int) -> int:
        for i in range(len(nums) - 1, -1, -1):
            if threshold < nums[i]:
                return i

        return -1
