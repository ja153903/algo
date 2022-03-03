"""
Given two strings text1 and text2, return the length of their longest common subsequence. If there is no common subsequence, return 0.

A subsequence of a string is a new string generated from the original string with some characters (can be none) deleted without changing the relative order of the remaining characters.

- For example, "ace" is a subsequence of "abcde".

A common subsequence of two strings is a subsequence that is common to both strings.

=== Solution ===

To solve this we should think in a similar vein to comparing the strings on a matrix where
the row is text1 and the column going down is text2

For example: text1 = "abcde", text2 = "ace"

  0 a b c d e
0 0 0 0 0 0 0
a 0 1 1 1 1 1
c 0 1 1 2 2 2
e 0 1 1 2 2 3

What we're seeing here is that when we compare them in a matrix, we can keep tabs
on how long the subsequence can go
"""


class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        n, m = len(text1), len(text2)

        dp = [[0 for _ in range(m + 1)] for _ in range(n + 1)]

        for i in range(0, n):
            for j in range(0, m):
                dp[i + 1][j + 1] = (
                    dp[i][j] + 1
                    if text1[i] == text2[j]
                    else max(dp[i + 1][j], dp[i][j + 1])
                )

        return dp[-1][-1]
