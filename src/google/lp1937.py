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

How can we optimize our previous approach?

Note that we probably never want to bother with absolute values of j - i
where this value is greater than 1.

Can we then introduce this logic here? Suppose that we only want to compare 
the difference between values next to each other? Is it possible to get
the same result?
[1, 2, 3],
[1, 5, 1],
[3, 1, 1]

Suppose that previous = [1, 2, 3]
Then the next row, how would we tabulate results?
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
        pass
