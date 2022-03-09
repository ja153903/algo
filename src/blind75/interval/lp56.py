from typing import List


class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        if not intervals:
            return []

        intervals.sort(key=lambda interval: (interval[0], interval[1]))

        result = []

        for interval in intervals:
            if not result:
                result.append(interval)
            else:
                top_start, top_end = result[-1]
                start, end = interval

                if top_end >= start:
                    result[-1] = [min(top_start, start), max(top_end, end)]
                else:
                    result.append(interval)

        return result
