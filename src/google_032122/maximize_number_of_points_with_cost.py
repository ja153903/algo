from typing import List


"""
This problem requires us to keep track of the previous row
and increment the current row based on that previous row

Note that there is a penalty with distance. This means that
the optimal solution is within 1 cell.

We can keep track of this by using two arrays that keep track of the rolling
max from the left and from the right.
"""


class Solution:
    def maxPoints(self, points: List[List[int]]) -> int:
        def get_previous_max_from_left(prev: List[int]) -> List[int]:
            result = [0] * len(prev)
            result[0] = prev[0]

            for i in range(1, len(prev)):
                result[i] = max(result[i - 1] - 1, prev[i])

            return result

        def get_previous_max_from_right(prev: List[int]) -> List[int]:
            result = [0] * len(prev)
            result[-1] = prev[-1]

            for i in range(len(prev) - 2, -1, -1):
                result[i] = max(result[i + 1] - 1, prev[i])

            return result

        if not points:
            return 0

        rows = len(points)
        cols = len(points[0])

        if cols == 1:
            return sum(sum(row) for row in points)

        if rows == 1:
            return max(points[0])

        prev = points[0]

        for i in range(1, rows):
            left, right, row = (
                get_previous_max_from_left(prev),
                get_previous_max_from_right(prev),
                [0] * cols,
            )
            for col in range(cols):
                row[col] = points[i][col] + max(left[col], right[col])

            prev = list(row)

        return max(prev)
