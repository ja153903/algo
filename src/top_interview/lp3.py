"""
Given a string s, find the length of the longest substring without repeating characters.

=== Solution ===
We can keep track of where the characters are in map.
Every time we see a character we've already seen before, we should update some variable
which holds our start.
"""
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        seen = {}

        max_len, j = 0, 0

        for i, val in enumerate(s):
            if val in seen:
                # if we've seen a character before, then the start j
                # should either be where it is now, or where it was previously seen + 1.
                # the reason we do this check is because a character could show up at the end
                # but was first entered in the beginning.
                # this means that j would then be pushed all the way back to the start when it shouldn't be
                j = max(j, seen[val] + 1)

            seen[val] = i
            max_len = max(max_len, i - j + 1)

        return max_len

