"""
Reverse bits of a given 32 bits unsigned integer.
"""


class Solution:
    def reverseBits(self, n: int) -> int:
        if n == 0:
            return 0

        result = 0

        # assume that we're going to work with 32 bits
        for _ in range(0, 32):
            # do a left shift to push the bits in result up
            result = result << 1

            # add 1 if necessary
            if (n & 1) == 1:
                result += 1

            # right shift n
            n = n >> 1

        return result
