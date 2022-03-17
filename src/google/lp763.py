from typing import List
from collections import defaultdict


class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        """
        You are given a string s. We want to partition the string into as many parts as possible so that each letter appears in at most one part.

        Note that the partition is done so that after concatenating all the parts in order, the resultant string should be s.

        Return a list of integers representing the size of these parts.

        === approach ===

        Construct the string such that we're keeping track of intervals.
        """

        mp = defaultdict(list)

        for i, ch in enumerate(s):
            if ch not in mp:
                mp[ch] = [i, i]
            else:
                mp[ch][-1] = i

        intervals = list(mp.values())

        intervals.sort(key=lambda interval: (interval[0], interval[1]))

        merged = [intervals[0]]

        for i in range(1, len(intervals)):
            top = merged[-1]
            current = intervals[i]

            if top[-1] >= current[0]:
                top[-1] = max(top[-1], current[1])
            else:
                merged.append(current)

        return [end - start + 1 for start, end in merged]

    def optimal(self, s: str) -> List[int]:
        rightmost = {ch: i for i, ch in enumerate(s)}
        result = []

        left, right = 0, 0

        for i, ch in enumerate(s):
            right = max(right, rightmost[ch])

            if i == right:
                result.append(right - left + 1)
                left = i + 1

        return result
