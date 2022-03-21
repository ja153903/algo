from typing import List
import heapq
import collections

"""
When dealing with top k problems, never push all items into the heap.
The easiest way to do this is by making sure that if we currently greater than k
we would pop the min element from the heap so we still have top k

Here's an example with Top K Frequent Elements
"""


class MinHeapPQWrapper:
    def __init__(self, num: int, count: int) -> None:
        self.num = num
        self.count = count

    def __lt__(self, other) -> bool:
        return self.count < other.count


class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counter = collections.Counter(nums)

        pq = []

        for key, value in counter.items():
            heapq.heappush(pq, MinHeapPQWrapper(key, value))
            if len(pq) > k:
                # this way we always pop out the smallest one
                heapq.heappop(pq)

        return [obj.num for obj in pq]
