"""
A strobogrammatic number is a number that looks the same when rotated 180 degrees (looked at upside down).

6 -> 9, 9 -> 6, 8 -> 8, 0 -> 0

Reverse and then flip, see if the same
"""


class Solution:
    def isStrobogrammatic(self, num: str) -> bool:
        mp = {"6": "9", "9": "6"}
        strobo_nums = set(["0", "1", "6", "8", "9"])

        reverse = num[::-1]

        flipped = []

        for ch in reverse:
            if ch not in strobo_nums:
                return False

            flipped.append(mp.get(ch, ch))

        return "".join(flipped) == num
