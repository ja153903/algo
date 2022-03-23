from typing import List
from collections import defaultdict


"""
--------
Approach
--------

We can keep track of the frequencies of each xy coordinate pair.
This will help us when we're tabulating the number of squares.
This is going to be necessary because when we count the number of squares
we count each coorindate pair as a unique point.

We also create this dictionary called x_coords which keeps track of the unique
x coordinates and adds the y coordinates to a list. This is going to be necessary
when we count the number of squares we have given a point.

The logic here being that we take the point we're given and find some y coordinate
so that we can form a vertical line. once this vertical line is formed, we would then
modify x coorindates to the left and right of it based on the length of the side (remember
that this is a square so one side length is the same as the other) and compute the product
of frequencies.
"""


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
