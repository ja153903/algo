"""
The invariant of the algorithms is two heaps, small and large, each represents half
of the current list. The length of smaller half is kept to be n / 2 at all times
and the length of the larger half is either (n/2) or (n/2 + 1) depending on n's parity.

This way we only need to peek the two heap's top numbers to calcualte the median.

Any time before we add a new number, there are two scenarios

1. length of (small, large) == (k, k)
2. length of (small, large) == (k, k + 1)

Afer adding the number, total (n + 1) numbers, they will become:

1. length of (small, large) == (k, k + 1)
2. length of (small, large) == (k + 1, k + 1)

Here we take the first scenario for example, we know the large will gain one more item
and small will remain the same size, but we cannot just push the item into large. What we
should do is we push the new number into small and pop the maximum item from small then push
it into large (all the pop and push here are heappop and heappush). By doing this kind of operations
for the scenarios we can keep our invariant.

Therefore to add a number, we have 3 O(lg n) heap operations.
"""
import heapq


class MedianFinder:
    def __init__(self):
        self.small = []  # max heap of smaller numbers
        self.large = []  # min heap of larger numbers

    def addNum(self, num: int) -> None:
        if len(self.small) == len(self.large):
            # In this case, we push the new number in to the max heap of small numbers
            # and then pop the max value from the small heap and push that value into
            # the min heap of large numbers
            heapq.heappush(self.large, -heapq.heappushpop(self.small, -num))
        else:
            # if at any point, the large heap has more values
            # then we push the number into the min heap of large values and pop the smallest
            # number from the min heap and push that into the max heap
            heapq.heappush(self.small, -heapq.heappushpop(self.large, num))

    def findMedian(self) -> float:
        if len(self.small) == len(self.large):
            return float(self.large[0] - self.small[0]) / 2
        else:
            return float(self.large[0])
