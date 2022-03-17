class Solution:
    def addBinary(self, a: str, b: str) -> str:
        result = []
        carry = 0

        i, j = len(a) - 1, len(b) - 1

        while i >= 0 and j >= 0:
            current = carry

            current += int(a[i])
            current += int(b[j])

            result.append(str(current % 2))
            carry = current // 2

            i -= 1
            j -= 1

        while i >= 0:
            current = carry

            current += int(a[i])

            result.append(str(current % 2))
            carry = current // 2

            i -= 1

        while j >= 0:
            current = carry

            current += int(b[j])

            result.append(str(current % 2))
            carry = current // 2

            j -= 1

        if carry > 0:
            result.append(str(carry))

        return "".join(reversed(result))
