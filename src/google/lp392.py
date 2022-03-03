"""
Given two strings s and t, return true if s is a subsequence of t, or false otherwise.

A subsequence of a string is a new string that is formed from the original string by deleting some (can be none) 
of the characters without disturbing the relative positions of the remaining characters. 
(i.e., "ace" is a subsequence of "abcde" while "aec" is not).
"""
from collections import deque


class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        if not s:
            return True

        if not t:
            return False

        s_deque = deque()

        for ch in s:
            s_deque.append(ch)

        for ch in t:
            if len(s_deque) == 0:
                return True

            if ch == s_deque[0]:
                s_deque.popleft()

        return len(s_deque) == 0
