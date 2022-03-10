"""
Consider this input string abcdbea

1. j=0 till the first d
2. j=1 as soon as the second b is spotted (i=4)
3. Now when second a is spotted (i=6), j will move back without the max condition and it'll end up creating a bigger substring.
As the OP already says, move j ONLY in the forward direction & hence, the j = Math.max(j, map.get(s.charAt(i)) + 1);
"""
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if not s:
            return 0

        mp = {}
        mx = 0
        j = 0

        for i, ch in enumerate(s):
            if ch in mp:
                # the next start point of the window is the max between
                # the current start point j or the previous index we say the character + 1
                j = max(j, mp[ch] + 1)

            mp[ch] = i
            mx = max(mx, i - j + 1)

        return mx
