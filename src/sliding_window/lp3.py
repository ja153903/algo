"""
Given a string s, find the length of the longest substring without repeating characters.

Algorithm
=========
We want to keep track of the longest substring without repeating characters.
"""
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        maxlen, start = 0, 0

        seen = {}

        for end, val in enumerate(s):
            if val in seen:
                start = max(start, seen[val] + 1)

            seen[val] = end
            maxlen = max(maxlen, end - start + 1)

        return maxlen
