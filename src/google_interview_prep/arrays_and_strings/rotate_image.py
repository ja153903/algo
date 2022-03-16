from typing import List


class Solution:
    # This is clockwise rotation
    # To do counter clockwise rotation, just swap first and then do reverse
    def rotate(self, matrix: List[List[int]]) -> None:
        """Do this in-place"""
        i, j = 0, len(matrix) - 1

        while i < j:
            matrix[i], matrix[j] = matrix[j], matrix[i]
            i += 1
            j -= 1

        for i in range(len(matrix)):
            for j in range(i + 1, len(matrix[i])):
                matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]

