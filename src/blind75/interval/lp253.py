from typing import List


class Solution:
    """
    I think the explanation is too complex and big for something that it's not that complicated. 
    What the algorithm is doing is checking how many meetings begin before the earliest-ended meeting ends. 
    If, for instance, 3 meetings have started before the earliest possible meeting end, than we need 3 rooms. 
    Sorting the arrays helps in two things: first of all you can easily get the earliest meetings end time,
    and secondly, it allows you to start looking for meetings ends only from next element in the ends array 
    when you find some meeting start that is after the current end, 
    because all other meeting ends before the current in the sorted array will also be before the current meeting start. 
    So you just have to run 1 time over each array.
    """

    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        n = len(intervals)
        starts, ends = [0] * n, [0] * n
        for i in range(len(intervals)):
            starts[i] = intervals[i][0]
            ends[i] = intervals[i][1]

        starts.sort()
        ends.sort()

        rooms = 0
        ends_itr = 0

        for i in range(len(starts)):
            if starts[i] < ends[ends_itr]:
                rooms += 1
            else:
                ends_itr += 1

        return rooms
