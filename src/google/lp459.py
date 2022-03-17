"""
So for this problem, if we  have a string of odd length,
the only way we can paste is if there is only 1 unique character.

Otherwise if we have an a odd length, we return false

=== Explanation ===
Consider a string S="helloworld". Now, given another string T="lloworldhe", can we figure out if T is a rotated version of S? Yes, we can! We check if S is a substring of T+T.
"""


class Solution:
    def repeatedSubstringPattern(self, s: str) -> bool:
        if len(s) <= 1:
            return False

        uniq = set(s)

        if len(uniq) == 1:
            return True

        for i in range(2, len(s) // 2 + 1):
            copies = len(s) // i

            if s[:i] * copies == s:
                return True

        return False

    def clever(self, s: str) -> bool:
        if not s:
            return False

        # concatenate string
        ss = s + s

        # remove first and last characters
        ss = ss[1:-1]

        # if by concatenating string, we can still find the character, then return true
        return ss.find(s) != -1
