from typing import List


class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        if not nums:
            return []

        result = []

        n = len(nums)

        nums.sort()

        for i in range(n - 2):
            if i == 0 or (i > 0 and nums[i] != nums[i - 1]):
                j, k = i + 1, n - 1

                while j < k:
                    target = nums[j] + nums[k]

                    if target == -nums[i]:
                        result.append([nums[i], nums[j], nums[k]])

                        while j < k and nums[j] == nums[j + 1]:
                            j += 1

                        while j < k and nums[k] == nums[k - 1]:
                            k -= 1

                        j += 1
                        k -= 1
                    elif target < -nums[i]:
                        j += 1
                    else:
                        k -= 1

        return result
