from typing import List


"""
Intuition for this problem from lee215 on LeetCode

We need to jump higher and lower alternately to the end.

Take [5,1,3,4,2] as example.

If we start at 2,
we can jump either higher first or lower first to the end,
because we are already at the end.
higher(2) = true
lower(2) = true

If we start at 4,
we can't jump higher, higher(4) = false
we can jump lower to 2, lower(4) = higher(2) = true

If we start at 3,
we can jump higher to 4, higher(3) = lower(4) = true
we can jump lower to 2, lower(3) = higher(2) = true

If we start at 1,
we can jump higher to 2, higher(1) = lower(2) = true
we can't jump lower, lower(1) = false

If we start at 5,
we can't jump higher, higher(5) = false
we can jump lower to 4, lower(5) = higher(4) = false
"""
class Solution:
    def oddEvenJumps(self, arr: List[int]) -> int:
        # if odd numbered jump, then jump to an index j such that arr[i] <= arr[j] and arr[j] is the smallest possible value
        # if there are multiple of such values, then jump to the smallest such index j
        # if even numbered jump, jump to an index such that arr[i] >= arr[j] and arr[j] is the largest possible value
        # if there are multiple of such values, then jump to the smallest such index j

        n = len(arr)

        next_higher, next_lower = [0] * n, [0] * n


        # In essence, we're trying to find the next greater element
        # this stack tries to accumulate the next minimum larger value
        stack = []
        for _, idx in sorted([num, idx] for idx, num in enumerate(arr)):
            while stack and stack[-1] < idx:
                next_higher[stack.pop()] = idx
            stack.append(idx)

        # In essence, we're trying to find the next greater element
        # this stack tries to accumulate the next maximum smaller value
        stack = []
        for _, idx in sorted([-num, idx] for idx, num in enumerate(arr)):
            while stack and stack[-1] < idx:
                next_lower[stack.pop()] = idx
            stack.append(idx)

        higher, lower = [0] * n, [0] * n
        higher[-1] = lower[-1] = 1

        for i in range(n - 2, -1, -1):
            # since we always alternate, higher[i] is going to be derived from lower but
            # we're going to be checking the next_higher index
            higher[i] = lower[next_higher[i]]

            # similar logic here
            lower[i] = higher[next_lower[i]]

        return sum(higher)
