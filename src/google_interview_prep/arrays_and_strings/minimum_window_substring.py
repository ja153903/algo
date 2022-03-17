"""
Given two strings s and t of lengths m and n respectively, 
return the minimum window substring of s such that every character in t 
(including duplicates) is included in the window.
If there is no such substring, return the empty string "".

The testcases will be generated such that the answer is unique.

A substring is a contiguous sequence of characters within the string.
"""
from collections import Counter


class Solution:
    def minWindow(self, s: str, t: str) -> str:
        counter = Counter(t)
        target = len(t)

        start = 0
        min_window = ""

        for end in range(len(s)):
            if counter.get(s[end], 0) > 0:
                target -= 1

            counter[s[end]] -= 1

            while target == 0:
                current_window_length = end - start + 1

                if not min_window or len(min_window) > current_window_length:
                    min_window = s[start : end + 1]

                counter[s[start]] += 1

                if counter[s[start]] > 0:
                    target += 1

                start += 1

        return min_window
