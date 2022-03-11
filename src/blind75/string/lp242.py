from collections import Counter


class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        s_cntr = Counter(s)

        for ch in t:
            if ch not in s_cntr or s_cntr[ch] == 0:
                return False

            s_cntr[ch] -= 1

        return sum(s_cntr.values()) == 0

