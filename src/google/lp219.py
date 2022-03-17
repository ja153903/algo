from typing import List
from collections import defaultdict


class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        """
        One possible approach we can take is to keep track of the indices in the hashmap.

        if the distance between the current index and the index we've seen before is k, then return true
        """
        seen = defaultdict(list)

        for i, num in enumerate(nums):
            if num in seen:
                seen_idx = seen[num][-1]
                if i - seen_idx <= k:
                    return True

            seen[num].append(i)

        return False
