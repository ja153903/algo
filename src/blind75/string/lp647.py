"""
We can also use the technique from lp5 here when we were trying to look for the longest palindrome.
"""


class Solution:
    def countSubstrings(self, s: str) -> int:
        count = 0

        for i in range(len(s)):
            pal1 = self.get_palindrome(s, i, i)
            pal2 = self.get_palindrome(s, i, i + 1)

            count += pal1 + pal2

        return count

    def get_palindrome(self, s: str, i: int, j: int) -> int:
        n = len(s)

        count = 0

        while i >= 0 and j < n and s[i] == s[j]:
            count += 1

            i -= 1
            j += 1

        return count
