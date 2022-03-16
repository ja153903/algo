"""
Given a string s, find the length of the longest substring without repeating characters.
"""
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        maxlen, start, end = 0, 0, 0

        mp = {}

        while end < len(s):
            if s[end] in mp:
                start = max(start, mp[s[end]] + 1)

            mp[s[end]] = end
            maxlen = max(maxlen, end - start + 1)
            end += 1


        return maxlen
