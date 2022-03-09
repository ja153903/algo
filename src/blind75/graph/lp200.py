"""
Given an m x n 2D binary grid grid which represents a map of '1's (land) and '0's (water),
return the number of islands.

An island is surrounded by water and is formed by connecting adjacent lands horizontally or vertically. 
You may assume all four edges of the grid are all surrounded by water.

=== Solution ===
To solve this problems, we should do DFS around when the current character is land.
"""
from typing import List


class Solution:
    def numIslands(self, grid: List[List[int]]) -> int:
        if not grid:
            return 0

        rows, cols = len(grid), len(grid[0])
        islands = 0

        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == "1":
                    self.dfs(grid, i, j)
                    islands += 1

        return islands

    def dfs(self, grid: List[List[int]], i: int, j: int):
        rows, cols = len(grid), len(grid[0])
        if i < 0 or j < 0 or i >= rows or j >= cols or grid[i][j] != "1":
            return

        grid[i][j] = "2"

        self.dfs(grid, i + 1, j)
        self.dfs(grid, i - 1, j)
        self.dfs(grid, i, j + 1)
        self.dfs(grid, i, j - 1)
