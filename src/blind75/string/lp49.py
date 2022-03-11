from typing import List
from collections import defaultdict


class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagrams = defaultdict(list)

        for s in strs:
            srtd = sorted(s)

            anagrams["".join(srtd)].append(s)

        return list(anagrams.values())
