class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        """
        There is also a trick to this question
        if we can do n & (n - 1) == 0
        """
        if n < 0:
            return False

        count = 0

        while n:
            if n & 1:
                count += 1

            n >>= 1

        return count == 1
