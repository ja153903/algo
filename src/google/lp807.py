from typing import List


class Solution:
    def maxIncreaseKeepingSkyline(self, grid: List[List[int]]) -> int:
        rows, cols = len(grid), len(grid[0])

        mrows = [0] * rows
        mcols = [0] * cols

        for i in range(rows):
            mrows[i] = max(grid[i])
            for j in range(cols):
                mcols[j] = max(mcols[j], grid[i][j])

        result = 0

        for i in range(rows):
            for j in range(cols):
                result += min(mrows[i], mcols[j]) - grid[i][j]

        return result
