from typing import List


class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        result = []
        if not nums:
            return result

        start = 0

        for i in range(1, len(nums)):
            if abs(nums[i] - nums[i - 1]) == 1:
                continue
            else:
                if i - 1 == start:
                    result.append(str(nums[start]))
                else:
                    result.append(f"{nums[start]}->{nums[i - 1]}")

                start = i

        if start == len(nums) - 1:
            result.append(str(nums[start]))
        else:
            result.append(f"{nums[start]}->{nums[-1]}")

        return result
