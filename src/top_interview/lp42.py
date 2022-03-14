from typing import List


"""
Given n non-negative integers representing an elevation map where the width of each bar is 1, 
compute how much water it can trap after raining.

=== Solution ===
height = [0,1,0,2,1,0,1,3,2,1,2,1]

We can approach this with a two pointer approach. Keeping track of the maximum
value on the left and right.
"""
class Solution:
    def trap(self, height: List[int]) -> int:
        max_left, max_right = height[0], height[-1]

        i, j = 0, len(height) - 1

        result = 0

        while i < j:
            if height[i] < height[j]:
                if max_left < height[i]:
                    max_left = height[i]
                else:
                    result += max_left - height[i]

                i += 1
            else:
                if max_right < height[j]:
                    max_right = height[j]
                else:
                    result += max_right - height[j]

                j -= 1

        return result

