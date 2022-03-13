from typing import List


"""
You are given an m x n integer matrix points.
Starting with 0 points, you want to maximize the number
of points you can get from the matrix.

To gain points, you must pick one cell in each row. Picking the cell
at coordinate (r, c) will add points[r][c] to your score.

However, you will lose points if you pick a cell too far from the cell
that you picked in the previous row. For every two adjacent rows r and
r + 1 (where 0 <= r <= m - 1), picking cells at coordinates (r, c1) and
(r + 1, c2) will subtract abs(c1 - c2) from your score

Return the maximum number of points you can achieve.

=== Approach ===
From what we can see, the maximum number of points can be derived from
the previous row and we just check it against the current row.
So we do something like previous_row = points[0] and then check
every row.

=== Optimal ===
The idea with our optimal solution is that given some index j
we're choosing choosing the max possible value from either j's left or right.
We do this by precomputing the array of max values minus 1 from the left and from the right
"""


class Solution:
    def brute_force(self, points: List[List[int]]) -> int:
        previous = points[0]

        for i in range(1, len(points)):
            for j, num in enumerate(points[i]):
                for prev_num in previous:
                    points[i][j] = max(points[i][j], num + prev_num - abs(j - i))
            previous = points[i]

        return max(previous)

    def maxPoints(self, points: List[List[int]]) -> int:
        m, n = len(points), len(points[0])

        if m == 1:
            return max(points[0])

        if n == 1:
            return sum(sum(row) for row in points)

        def left(lst: List[int]) -> int:
            result = [lst[0]] + [0] * (n - 1)

            for i in range(1, n):
                result[i] = max(result[i - 1] - 1, lst[i])

            return result

        def right(lst: List[int]) -> int:
            result = [0] * (n - 1) + [lst[-1]]

            for i in range(n - 2, -1, -1):
                result[i] = max(result[i + 1] - 1, lst[i])

            return result

        previous = points[0]

        for i in range(m - 1):
            lft, rgt, cur = left(previous), right(previous), [0] * n

            for j in range(n):
                cur[j] = points[i + 1][j] + max(lft[j], rgt[j])

            previous = list(cur)

        return max(previous)
