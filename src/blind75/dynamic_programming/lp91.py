"""
=== Solution ===
dp = [0] * (len(s) + 1)
dp[0] = 1
dp[1] = 1 if 1 <= s[0] <= 9 else 0
"""


class Solution:
    def numDecodings(self, s: str) -> int:
        dp = [0] * (len(s) + 1)
        dp[0] = 1
        dp[1] = 1 if 1 <= int(s[0]) <= 9 else 0

        for i in range(2, len(s) + 1):
            if 1 <= int(s[i - 1 : i]) <= 9:
                dp[i] += dp[i - 1]

            if 10 <= int(s[i - 2 : i]) <= 26:
                dp[i] += dp[i - 2]

        return dp[-1]

    def numDecodings_space_optimal(self, s: str) -> int:
        a = 1
        b = 1 if 1 <= int(s[0]) <= 9 else 0
        c = 0

        for i in range(2, len(s) + 1):
            if 1 <= int(s[i - 1 : i ]) <= 9:
                c += b

            if 10 <= int(s[i - 2 : i]) <= 26:
                c += a

            a, b, c = b, c, 0

        return b
