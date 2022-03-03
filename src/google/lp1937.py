"""
You are given an m x n integer matrix points (0-indexed). Starting with 0 points, you want to maximize the number of points you can get from the matrix.

To gain points, you must pick one cell in each row. Picking the cell at coordinates (r, c) will add points[r][c] to your score.

However, you will lose points if you pick a cell too far from the cell that you picked in the previous row.
For every two adjacent rows r and r + 1 (where 0 <= r < m - 1), picking cells at coordinates (r, c1) and (r + 1, c2) will subtract abs(c1 - c2) from your score.

Return the maximum number of points you can achieve.

abs(x) is defined as:
- x for x >= 0.
- -x for x < 0.

=== Explanation ===

The idea behind this solution starts with figuring out what the brute force approach is.

Given that we want to maximize the number of points you can get from the matrix, we should first start with initializing our first previous row.
For this, we can say that the previous row is the first row. This allows us to start our iteration from the second row onwards.

previous = points[0]

for i in range(rows - 1):
    current = [0] * cols

    for j in range(cols):
        # we should then have to compute the following:
        current_max = -1
        for k in range(cols):
            current_max = max(current_max, previous[j] + points[i + 1][k] - abs(j - k))
        
        current[j] = current_max
    
    previous = list(current)

However, this solution causes it to be O(m * n^2).

To improve on this solution, we can implement the following idea.

We can split the previous array into two running max valuations.

We can start from the left or from the right and compute the maximum values around some index j.

We should then precompute these arrays based on the following idea:

result[i] = max(result[i - 1] - 1, row[i]) for left-to-right iteration

and 

result[i] = max(result[i + 1] - 1, row[i]) for right-to-left iteration

The reason we do this is because we've already selected the largest possible selection in the previous result
so we have to subtract by 1 to account for the shift in index.
"""
from typing import List


class Solution:
    def maxPoints(self, points: List[List[int]]) -> int:
        rows, cols = len(points), len(points[0])

        if rows == 1:
            return max(points[0])

        if cols == 1:
            return sum(sum(row) for row in points)

        def left(row: List[int]) -> List[int]:
            result = [row[0]] + [0] * (cols - 1)

            for i in range(1, cols):
                result[i] = max(result[i - 1] - 1, row[i])

            return result

        def right(row: List[int]) -> List[int]:
            result = [0] * (cols - 1) + [row[-1]]

            for i in range(cols - 2, -1, -1):
                result[i] = max(result[i + 1] - 1, row[i])

            return result
        
        prev = points[0]

        for i in range(rows - 1):
            left_max_values = left(prev)
            right_max_values = right(prev)

            current = [0] * cols

            for j in range(cols):
                current[j] = points[i + 1][j] + max(left_max_values[j], right_max_values[j])

            prev = list(current)

        return max(prev)
