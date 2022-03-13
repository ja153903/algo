from typing import List
from collections import deque


class Solution:
    def shortestPath(self, grid: List[List[int]], k: int) -> int:
        """
        m x n matrix. Each cell is either 0 or 1 where 1 means there's an obstacle
        We can move up, down, left, or right from and to an empty cell in one step.

        Return the minimum number of steps to walk from the upper left corner (0, 0)
        to the lower right corner (m - 1, n - 1) given that you can eliminate at most
        k obstacles . If it's not possible, then return -1

        === Thoughts ===
        - since we can move in 4 directions and we're in need of an early stop,
          this problem should use some sort of DFS or BFS.
        - In our walk, we should keep track of nodes we've visited before and also
          the current value of k.
        
        === Solution ===
        The idea with this solution is to keep track of the number of obstacles that we
        have left to destroy while also keeping track of the current row and column with
        the number of steps.

        Then we also keep track in our visited state the row, column, and the number of
        obstacles left to destroy at that point.
        """

        rows, cols = len(grid), len(grid[0])

        if rows == 1 and cols == 1:
            return 0

        # Keep track of current row, col, num_obstacles_left_to_elim, steps
        queue = deque([(0, 0, k, 0)])

        # In path, keep track of row, col, and num_obstcles_left_to_elim
        visited = set([(0, 0, k)])

        # if the number of obstacles is greater than the number of rows and cols
        # then we can just blow through all of them and take the shortest path
        # which is down the rows and across the columns
        if k > rows - 1 + cols - 1:
            return rows - 1 + cols - 1

        while queue:
            row, col, num_left_to_elim, steps = queue.popleft()

            for nrow, ncol in [
                (row + 1, col),
                (row - 1, col),
                (row, col + 1),
                (row, col - 1),
            ]:
                # do boundary check
                if nrow < 0 or ncol < 0 or nrow >= rows or ncol >= cols:
                    continue

                # Consider approach where we eliminate the obstacle
                if (
                    grid[nrow][ncol] == 1
                    and num_left_to_elim > 0
                    and (nrow, ncol, num_left_to_elim - 1) not in visited
                ):
                    visited.add((nrow, ncol, num_left_to_elim - 1))
                    queue.append((nrow, ncol, num_left_to_elim - 1, steps + 1))

                if (
                    grid[nrow][ncol] == 0
                    and (nrow, ncol, num_left_to_elim) not in visited
                ):
                    if nrow == rows - 1 and ncol == cols - 1:
                        return steps + 1

                    visited.add((nrow, ncol, num_left_to_elim))
                    queue.append((nrow, ncol, num_left_to_elim, steps + 1))
        return -1
