from typing import List
import heapq
import collections


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
