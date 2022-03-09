from typing import List


class Solution:
    """
    this problem is the same as finding the maximum number of non-overlapping intervals
    """
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        if not intervals:
            return 0

        intervals.sort(key=lambda interval: interval[1])
        end = intervals[0][1]
        count = 1

        for i in range(1, len(intervals)):
            if intervals[i][0] >= end:
                count += 1
                end = intervals[i][1]

        # the count we get is the maximum number of non-overlapping intervals
        # the minimum to remove is the complement
        return len(intervals) - count
