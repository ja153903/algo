from typing import List
from collections import Counter


class Solution:
    def findOriginalArray(self, changed: List[int]) -> List[int]:
        if not changed or len(changed) % 2 == 1:
            return []

        result = []

        changed.sort()

        counter = Counter(changed)

        for num in changed:
            if counter[num] > 0:
                if num * 2 in counter and counter[num * 2] > 0:
                    counter[num * 2] -= 1
                    counter[num] -= 1

                    if counter[num] >= 0:
                        result.append(num)
                    else:
                        return []

        return result if len(result) == len(changed) // 2 else []
