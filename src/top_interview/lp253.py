from typing import List


"""
Given an array of meeting time intervals, intervals where
intervals[i] = [start_i, end_i], return the minimum number
of conference rooms required.
"""
class Solution:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        start, end = [], []

        for s, e in intervals:
            start.append(s)
            end.append(e)

        start.sort()
        end.sort()

        rooms, end_itr = 0, 0

        for i in range(len(start)):
            if start[i] < end[end_itr]:
                rooms += 1
            else:
                end_itr += 1

        return rooms
