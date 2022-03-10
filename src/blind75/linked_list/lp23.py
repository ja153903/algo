from data_structures.list import ListNode

from typing import List, Optional
import heapq


"""
One brute force approach I can think of is to
use a heap to store all the items and pretty much
dot a heap sort => O(n lg k) time complexity
"""
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        # NOTE: This is the crucial portion
        ListNode.__lt__ = lambda self, other: self.val < other.val
        pq = []

        result = ListNode(0)
        runner = result

        for lst in lists:
            if lst:
                heapq.heappush(pq, lst)

        while pq:
            node = heapq.heappop(pq)
            runner.next = node
            runner = runner.next
            if node.next:
                heapq.heappush(pq, node.next)

        return result.next
