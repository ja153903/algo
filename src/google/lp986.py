from typing import List


"""
Two lists of pairwise disjoint intervals these lists are sorted

The intersection of two closed intervals is a set of real numbers
that are either empty or represented as a closed interval.

Input: firstList = [[0,2],[5,10],[13,23],[24,25]], secondList = [[1,5],[8,12],[15,24],[25,26]]
Output: [[1,2],[5,5],[8,10],[15,23],[24,24],[25,25]]

=== Retrospective ===

* Find the criss cross lock. If such a condition exists, then we can add it
* update the end we've already exhausted
"""


class Solution:
    def intervalIntersection(
        self, firstList: List[List[int]], secondList: List[List[int]]
    ) -> List[List[int]]:
        i, j = 0, 0
        f_len = len(firstList)
        s_len = len(secondList)

        result = []

        while i < f_len and j < s_len:
            f_start, f_end = firstList[i]
            s_start, s_end = secondList[j]

            if f_start <= s_end and s_start <= f_end:
                result.append([max(f_start, s_start), min(f_end, s_end)])

            # if the current f is already less than s, then this means we've exhausted this range
            if f_end <= s_end:
                i += 1
            else:
                j += 1

        return result
