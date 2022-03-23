from typing import List


"""
--------
Approach
--------

We can keep a counter for each number in the changed array.

For each item in the array, we can keep track if that num * 2 also
exists in the counter. If it does, make sure that the count matches up.

How do we take care of edge case 0?

We should sort the numbers here.
"""
from collections import Counter


class Solution:
    def findOriginalArray(self, changed: List[int]) -> List[int]:
        if not changed or len(changed) % 2 == 1:
            return []

        changed.sort()

        counter = Counter(changed)
        result = []

        for num in changed:
            if counter[2 * num] > 0 and counter[num] > 0:
                counter[2 *  num] -= 1
                counter[num] -= 1

                if counter[num] >= 0:
                    result.append(num)

        if len(result) == len(changed) // 2:
            return result

        return []

