from typing import List
from collections import deque


class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        dq = deque()
        result = []

        for i, val in enumerate(nums):
            # remove indices that are out of scope
            if dq and dq[0] < i - k + 1:
                dq.popleft()

            # remove intermediate values that will never be chosen
            while dq and nums[dq[-1]] < val:
                dq.pop()

            dq.append(i)
            if i >= k - 1:
                # we only start inserting values into the result once we've gone through k
                result.append(nums[dq[0]])

        return result
