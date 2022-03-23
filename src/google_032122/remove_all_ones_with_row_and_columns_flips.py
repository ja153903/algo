from typing import List


class Solution:
    def removeOnes(self, grid: List[List[int]]) -> bool:
        # in this problem, we should look for all the columns in the first row that have a 1
        # those are columns we should flip
        # then once we flip those columns, we can linearly scan to see if we have all 1s or all 0s
        # if there exists any row that doesn't have all 1s or all 0s, then we return false
        # otherwise we return true
        rows, cols = len(grid), len(grid[0])

        cols_to_flip = set()

        for col in range(cols):
            if grid[0][col] == 1:
                cols_to_flip.add(col)

        for col in cols_to_flip:
            for i in range(rows):
                grid[i][col] = 1 if grid[i][col] == 0 else 0

        for row in grid:
            row_sum = sum(row)

            if row_sum != cols and row_sum != 0:
                return False

        return True

