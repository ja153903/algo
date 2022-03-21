from typing import List


"""
Reversing Bits

Approach
--------

It might be a good idea to ask if we're working with a 32-bit or 64-bit list.

We iterate over all the possible bit positions.
For each bit position, we do a left shift on our result variable to create space
for the bit to add if the last bit of the number we're trying to reverse is 1.
Once we know that, we increment the result and then do a right shift on the number
we're reversing
"""


def reverse_bits(n: int, bits: int) -> int:
    if n == 0:
        return 0

    result = 0

    for _ in range(bits):
        result <<= 1

        # if the last bit is 1
        if (n & 1) == 1:
            result += 1

        n >>= 1

    return result


"""
Hamming weight is a way to determine how to count the number of 1 bits
within a number
"""


def hamming_weight(n: int) -> int:
    result = 0

    while n > 0:
        # we again take advantage of this check
        if n & 1 == 1:
            result += 1

        n >>= 1

    return result


"""
Finding missing numbers

Approach
--------

For this problem, we are guaranteed that only 1 number
is missing from the range of [0, n].

Given that this array is filled with numbers within the [0, n],
we can take advantage of the XOR operator.

The XOR operator is commutative. This means that doing 0 ^ 1 ^ 0 is the same as doing 0 ^ 0 ^ 1.

So we can use this strategy to reduce all values and indices and figure out what's missing.
"""


def missing_number(nums: List[int]) -> int:
    xor, i = 0, 0

    while i < len(nums):
        xor = xor ^ i ^ nums[i]
        i += 1

    return xor ^ i


"""
Bit Tricks
----------

Finding the carry between an operation between two numbers (x & y) << 1

Seeing if the rightmost bit is set: n & 1 == 1
"""
