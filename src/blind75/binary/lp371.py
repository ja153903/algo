"""
Given two integers a and b, return the sum of the two integers without using the operators + and -.

=== Solution ===

Typically, if you have a problem where they're asking you not to use + or - operators,
this means they want you to use some sort of bit manipulation

Suppose that we have the following example:

3 => 011
2 => 010

We expect 5 => 101 to be our result. How do we get there?

Now look at what happens when we do an XOR operation?

3 ^ 2 => 001 but notice that this doesn't help us with the carry
How can we then find the carry? The carry is generated when both the bits are set.
So for example 3 & 2 => 010, notice how the second bit is set here. To finally generate
the correct carry, we should then shift this over to the left.
Our carry is then (3 & 2) << 1 which comes out to 100.

Since our carry is nonzero, we should then do XOR again until the carry is zero.
"""


class Solution:
    def getSum(self, a: int, b: int) -> int:
        # This solution is a modified one to take care of negative numbers
        x, y = abs(a), abs(b)

        if x < y:
            return self.getSum(b, a)

        sign = 1 if a > 0 else -1

        if a * b >= 0:
            while y:
                x, y = x ^ y, (x & y) << 1
        else:
            while y:
                x, y = x ^ y, ((~x) & y) << 1

        return x * sign
