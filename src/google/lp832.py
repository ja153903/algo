from typing import List

"""
Given an n x n binary matrix image, flip the image horizontally, then invert it, and return the resulting image.

flipping image horizontally means we're reversing the row

inverting it means that we're flipping 0s to 1s and 1s to 0s
"""


class Solution:
    def flipAndInvertImage(self, image: List[List[int]]) -> List[List[int]]:
        result = []

        for row in image:
            result.append(1 if col == 0 else 0 for col in reversed(row))

        return result
