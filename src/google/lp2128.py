from typing import List


"""
You are given m x n binary matrix grid

In one operation, you can choose any row or column and flip each value in that row or column

Return true if it's possible to remove all 1's from grid using any number of operations

=== Solution ===
To achieve this solution, we should flip the column where there is a 1 in the first row.
Once we do this, we cannot flip columns again. So, after this, we then should only flip the rows
if they are all 1s. If there exist a row with both 1s and 0s then it's not possible to do this
"""


class Solution:
    def removeOnes(self, grid: List[List[int]]) -> bool:
        rows, cols = len(grid), len(grid[0])

        cols_to_flip = set()

        for i in range(cols):
            if grid[0][i] == 1:
                cols_to_flip.add(i)

        for col in cols_to_flip:
            for row in range(rows):
                grid[row][col] = 1 if grid[row][col] == 0 else 0

        for i in range(1, rows):
            row_sum = sum(grid[i])
            if row_sum != 0 and row_sum != cols:
                return False

        return True
