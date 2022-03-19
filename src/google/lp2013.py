from typing import List
from collections import defaultdict


class DetectSquares:
    def __init__(self):
        self.frequency = defaultdict(int)
        self.x_coords = defaultdict(list)

    def add(self, point: List[int]) -> None:
        x, y = point
        self.frequency[(x, y)] += 1
        self.x_coords[x].append(y)

    def count(self, point: List[int]) -> int:
        x1, y1 = point
        ans = 0

        for y2 in self.x_coords[x1]:
            if y2 == y1:
                continue

            side_len = abs(y2 - y1)

            # given the current information we have, we have 1 line

            # This checks if we have lines on the left of the point
            x3, y3 = x1 - side_len, y1
            x4, y4 = x1 - side_len, y2

            ans += self.frequency[(x3, y3)] * self.frequency[(x4, y4)]

            # this checks if we have lines on the right of the point
            x3, y3 = x1 + side_len, y1
            x4, y4 = x1 + side_len, y2

            ans += self.frequency[(x3, y3)] * self.frequency[(x4, y4)]

        return ans
