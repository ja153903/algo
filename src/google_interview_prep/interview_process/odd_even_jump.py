from typing import List


class Solution:
    def oddEvenJumps(self, arr: List[int]) -> int:
        # if odd numbered jump, then jump to an index j such that arr[i] <= arr[j] and arr[j] is the smallest possible value
        # if there are multiple of such values, then jump to the smallest such index j
        # if even numbered jump, jump to an index such that arr[i] >= arr[j] and arr[j] is the largest possible value
        # if there are multiple of such values, then jump to the smallest such index j
        if not arr:
            return 0


        return result
