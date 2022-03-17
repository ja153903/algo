from collections import deque


class MovingAverage:
    def __init__(self, size: int):
        self.window = deque(maxlen=size)
        self.window_size = size
        self.current_size = 0
        self.sum = 0

    def next(self, val: int) -> float:
        if self.current_size < self.window_size:
            self.window.append(val)
            self.current_size += 1
            self.sum += val
        else:
            front = self.window.popleft()
            self.sum -= front
            self.window.append(val)
            self.sum += val
            
        return self.sum / self.current_size
            