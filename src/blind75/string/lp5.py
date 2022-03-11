from collections import deque


class Solution:
    def longestPalindrome(self, s: str) -> str:
        # one thing we can do is expand around a set of indices
        max_pal = ""

        for i in range(len(s)):
            pal1 = self.get_palindrome(s, i, i)
            pal2 = self.get_palindrome(s, i, i + 1)

            max_pal = max([max_pal, pal1, pal2], key=lambda s: len(s))

        return max_pal

    def get_palindrome(self, s: str, i: int, j: int) -> str:
        # expand around i and j
        n = len(s)

        pal = deque()

        while i >= 0 and j < n and s[i] == s[j]:
            if i == j:
                pal.append(s[i])
            else:
                pal.append(s[j])
                pal.appendleft(s[i])

            i -= 1
            j += 1

        return "".join(pal)

