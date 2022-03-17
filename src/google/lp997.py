from typing import List


class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        # reduce trust value by 1 to accomodate for indices
        outgoing = [0 for _ in range(n)]
        incoming = [0 for _ in range(n)]

        for u, v in trust:
            outgoing[u - 1] += 1
            incoming[v - 1] += 1

        # we need to find a person with outgoing as 0 and incoming as n - 1
        for i in range(n):
            if outgoing[i] == 0 and incoming[i] == n - 1:
                return i + 1

        return -1
