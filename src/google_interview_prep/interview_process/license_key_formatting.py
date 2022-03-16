"""
For this problem, we'll probably want to split by dashes
Then contract groups of k
"""
class Solution:
    def licenseKeyFormatting(self, s: str, k: int) -> str:
        chars = []
        result = []

        for group in s.split("-"):
            for ch in group:
                chars.append(ch)

        while chars:
            current = []
            for _ in range(k):
                if chars:
                    ch = chars.pop()
                    if ch.isalpha():
                        current.append(ch.upper())
                    else:
                        current.append(ch)
                else:
                    break

            result.append("".join(current[::-1]))

        return "-".join(result[::-1])

