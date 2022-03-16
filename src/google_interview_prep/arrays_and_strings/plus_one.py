from typing import List


class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        if not digits:
            return []
        
        digits[-1] += 1

        carry = 1 if digits[-1] >= 10 else 0
        if carry == 0:
            return digits

        digits[-1] %= 10

        for i in range(len(digits) - 2, -1, -1):
            digits[i] += carry
            carry = digits[i] // 10
            digits[i] %= 10

        if carry > 0:
            return [1] + digits

        return digits
