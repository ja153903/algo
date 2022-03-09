from typing import List


class Solution:
    def insert(
        self, intervals: List[List[int]], new_interval: List[int]
    ) -> List[List[int]]:
        result = []

        i = 0

        # add all the intervals ending before new interval
        while i < len(intervals) and intervals[i][1] < new_interval[0]:
            result.append(intervals[i])
            i += 1

        while i < len(intervals) and intervals[i][0] <= new_interval[1]:
            new_interval = [
                min(new_interval[0], intervals[i][0]),
                max(new_interval[1], intervals[i][1]),
            ]
            i += 1

        result.append(new_interval)

        while i < len(intervals):
            result.append(intervals[i])
            i += 1

        return result
