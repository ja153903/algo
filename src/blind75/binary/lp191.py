"""
Write a function that takes an unsigned integer and returns the number of '1' bits it has (also known as the Hamming weight).
"""


class Solution:
    def hammingWeight(self, n: int) -> int:
        result = 0

        while n > 0:
            if n & 1 == 1:
                result += 1
            n = n >> 1

        return result
