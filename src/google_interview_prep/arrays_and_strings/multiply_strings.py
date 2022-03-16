class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        if len(num1) < len(num2):
            num1, num2 = num2, num1

        result = 0
        mod = 1

        for i in range(len(num2) - 1, -1, -1):
            subresult, carry, k = 0, 0, 1
            for j in range(len(num1) - 1, -1, -1):
                current = carry

                value = int(num1[j]) * int(num2[i])
                current += value % 10
                carry = value // 10

                subresult += current * k
                k *= 10

            if carry > 0:
                subresult += carry * k

            result += subresult * mod
            mod *= 10

        return str(result)
