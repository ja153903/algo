from typing import List


class Solution:
    def canAttendMeetings(self, intervals: List[List[int]]) -> bool:
        if not intervals:
            return True

        # sort by the start time
        intervals.sort(key=lambda interval: interval[0])

        for i in range(1, len(intervals)):
            # if the current start time is less than
            # the previous end time means that it can
            # be merged.
            if intervals[i][0] < intervals[i - 1][1]:
                return False

        return True

