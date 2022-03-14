from typing import List


"""
=== Approach ===
To merge intervals, we should sort the intervals by the start.

For example, suppose that we have that result = [[1, 5]]
and the next interval we look at is [1, 6]

if see that the last interval in result has an end point greater than the current
interval's start, then this means that we have a merge candidate.
"""
class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        if not intervals:
            return []

        sorted_intervals = sorted(intervals, key=lambda interval: interval[0])

        result = [sorted_intervals[0]]

        for i in range(1, len(sorted_intervals)):
            current = sorted_intervals[i]
            top = result[-1]

            if top[-1] >= current[0]:
                # we can merge the intervals
                top[-1] = max(current[-1], top[-1])
            else:
                result.append(current)

        return result

