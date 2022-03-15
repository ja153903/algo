import heapq


class StockPrice:
    def __init__(self) -> None:
        self.timestamp = {}
        self.current_timestamp = 0

        self.max_heap = []
        self.min_heap = []

    def update(self, timestamp: int, price: int) -> None:
        self.current_timestamp = max(self.current_timestamp, timestamp)
        self.timestamp[timestamp] = price

        heapq.heappush(self.max_heap, (-price, timestamp))
        heapq.heappush(self.min_heap, (price, timestamp))

    def current(self) -> int:
        return self.timestamp.get(self.current_timestamp)

    def maximum(self) -> int:
        current_price, timestamp = heapq.heappop(self.max_heap)

        while -current_price != self.timestamp[timestamp]:
            current_price, timestamp = heapq.heappop(self.max_heap)

        heapq.heappush(self.max_heap, (current_price, timestamp))
        return -current_price

    def minimum(self) -> int:
        current_price, timestamp = heapq.heappop(self.min_heap)

        while current_price != self.timestamp[timestamp]:
            current_price, timestamp = heapq.heappop(self.min_heap)

        heapq.heappush(self.min_heap, (current_price, timestamp))
        return current_price
