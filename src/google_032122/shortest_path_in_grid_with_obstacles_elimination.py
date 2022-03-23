from typing import List


"""
You are given an m x n integer matrix grid where each cell is either 0 (empty) or 1 (obstacle). 
You can move up, down, left, or right from and to an empty cell in one step.

Return the minimum number of steps to walk from the upper left corner (0, 0) to the lower right corner (m - 1, n - 1) 
given that you can eliminate at most k obstacles. 

If it is not possible to find such walk return -1.

--------
Approach
--------
We can use a typical BFS approach to this problem.
However, we should also keep track of how many obstacles we have left to eliminate.
We should also keep track of this within our visited set.

This algorithm runs in O(n^2 * k) where n is the length of the grid and k is the quota we have
"""
from collections import deque


class Solution:
    def shortestPath(self, grid: List[List[int]], k: int) -> int:
        rows, cols = len(grid), len(grid[0])

        if rows == 1 and cols == 1:
            return 0

        queue = deque([(0, 0, k, 0)])
        visited = set([(0, 0, k)])

        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]

        # This is an edge case where we're able to
        # knock down every obstacle in our path
        if k > rows - 1 + cols - 1:
            return rows - 1 + cols - 1

        while queue:
            x, y, num_obstacles_left, steps = queue.popleft()

            for dx, dy in directions:
                nx = x + dx
                ny = y + dy

                if nx < 0 or ny < 0 or nx >= rows or ny >= cols:
                    continue

                # we can either break through an obstacle
                if (
                    grid[nx][ny] == 1
                    and num_obstacles_left - 1 >= 0
                    and (nx, ny, num_obstacles_left - 1) not in visited
                ):
                    queue.append((nx, ny, num_obstacles_left - 1, steps + 1))
                    visited.append((nx, ny, num_obstacles_left - 1))

                # or we can choose to go around it
                if grid[nx][ny] == 0 and (nx, ny, num_obstacles_left) not in visited:
                    if x == rows - 1 and y == cols - 1:
                        return steps + 1

                    queue.append((nx, ny, num_obstacles_left, steps + 1))
                    visited.append((nx, ny, num_obstacles_left))

        return -1
