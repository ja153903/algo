from collections import Counter


class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        maxf, start = 0, 0
        counter = Counter()

        for end in range(len(s)):
            counter[s[end]] += 1

            maxf = max(maxf, counter[s[end]])
            if end - start + 1 - maxf > k:
                counter[s[start]] -= 1
                start += 1

        return len(s) - start


