"""
You are given a stream of records about a particular stock. Each record contains a timestamp and the corresponding price of the stock at that timestamp.

Unfortunately due to the volatile nature of the stock market, the records do not come in order. Even worse, some records may be incorrect. Another record with the same timestamp may appear later in the stream correcting the price of the previous wrong record.

Design an algorithm that:

Updates the price of the stock at a particular timestamp, correcting the price from any previous records at the timestamp.
Finds the latest price of the stock based on the current records. The latest price is the price at the latest timestamp recorded.
Finds the maximum price the stock has been based on the current records.
Finds the minimum price the stock has been based on the current records.
Implement the StockPrice class:

StockPrice() Initializes the object with no price records.
void update(int timestamp, int price) Updates the price of the stock at the given timestamp.
int current() Returns the latest price of the stock.
int maximum() Returns the maximum price of the stock.
int minimum() Returns the minimum price of the stock.

--------
Approach
--------

Since we're consistently trying to find the maximum and minimum prices based on the record,
a data structure we can take advantage of is a heap.

We can sort this heap based on the timestamp. This way we can easily get the largest timestamp.
If we use a maxheap so that getting the current price is easy.

These types of problems where we need a max and a min could require two heaps
"""
import heapq


class StockPrice:
    def __init__(self):
        # this will serve as our source of truth
        self.timestamps = {}
        self.min_heap = []
        self.max_heap = []
        self.current_timestamp = 0

    def update(self, timestamp: int, price: int) -> None:
        self.current_timestamp = max(self.current_timestamp, timestamp)
        self.timestamps[timestamp] = price

        heapq.heappush(self.min_heap, (price, timestamp))
        heapq.heappush(self.max_heap, (-price, timestamp))

    def current(self) -> int:
        return self.timestamps[self.current_timestamp]

    def maximum(self) -> int:
        price, timestamp = heapq.heappop(self.max_heap)

        # suppose that we have this timestamp and price, but the records
        # we have in the hashmap are not the same, then we should
        # continually pop from the maxheap until we've reached
        # an accurate max
        while -price != self.timestamps[timestamp]:
            price, timestamp = heapq.heappop(self.max_heap)

        heapq.heappush(self.max_heap, (price, timestamp))

        return -price

    def minimum(self) -> int:
        price, timestamp = heapq.heappop(self.min_heap)

        # similar to what we had to do for the max heap
        # we should purge inaccurate minimum values
        while price != self.timestamps[timestamp]:
            price, timestamp = heapq.heappop(self.min_heap)

        heapq.heappush(self.min_heap, (price, timestamp))

        return price
