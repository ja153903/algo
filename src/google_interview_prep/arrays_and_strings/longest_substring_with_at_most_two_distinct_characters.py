"""
Given a string s, return the length of the longest substring that contains at most two distinct characters.

=== Approach ===
Use sliding window approach
"""
from collections import Counter


class Solution:
    def lengthOfLongestSubstringTwoDistinct(self, s: str) -> int:
        counter = Counter()

        start = 0
        maxlen = 0

        num_unique = 0

        for end in range(len(s)):
            if s[end] not in counter:
                num_unique += 1

            counter[s[end]] += 1

            if num_unique > 2:
                # if there are more than 2 unique values
                # then we have to move start up
                counter[s[start]] -= 1

                if counter[s[start]] == 0:
                    num_unique -= 1
                    del counter[s[start]]

                start += 1
            else:
                maxlen = max(maxlen, end - start + 1)

        return maxlen
