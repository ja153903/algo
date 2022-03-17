from typing import List
import heapq


class KthLargest:
    def __init__(self, k: int, nums: List[int]):
        self.k = k
        self.h = nums
        heapq.heapify(self.h)

        # we use a min heap here to keep 6 elements
        # removing the smallest ones leaving k largest
        while len(self.h) > k:
            heapq.heappop(self.h)

    def add(self, val: int) -> int:
        # we can safely push value in if length is less than k
        if len(self.h) < self.k:
            heapq.heappush(self.h, val)
        # if the current value we're trying to insert is greater than
        # the min value in the heap, then we replace the min value in the heap
        elif val > self.h[0]:
            heapq.heapreplace(self.h, val)

        # return the min value in the heap
        return self.h[0]
