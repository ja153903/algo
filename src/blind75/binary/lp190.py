"""
Reverse bits of a given 32 bits unsigned integer.
"""


class Solution:
    def reverseBits(self, n: int) -> int:
        if n == 0:
            return 0

        result = 0

        for i in range(0, 32):
            result = result << 1
            if (n & 1) == 1:
                result += 1

            n = n >> 1

        return result
