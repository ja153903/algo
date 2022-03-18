"""
Given a m * n matrix of ones and zeros, return how many square submatrices have all ones.
"""
from typing import List


class Solution:
    def countSquares(self, matrix: List[List[int]]) -> int:
        result = 0

        m, n = len(matrix), len(matrix[0])

        dp = [[0 for _ in range(n + 1)] for _ in range(m + 1)]

        for i in range(1, m + 1):
            for j in range(1, n + 1):
                if matrix[i - 1][j - 1] == 1:
                    dp[i][j] = min(dp[i - 1][j], dp[i][j - 1], dp[i - 1][j - 1]) + 1
                    result += dp[i][j]

        return result
