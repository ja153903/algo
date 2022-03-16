class Solution:
    def maxArea(self, height: List[int]) -> int:
        if not height:
            return 0

        i, j = 0, len(height) - 1
        maxarea = 0
        
        while i < j:
            left, right = height[i], height[j]
            area = min(left, right) * (j - i)

            maxarea = max(maxarea, area)

            if left < right:
                i += 1
            else:
                j -= 1

        return maxarea
