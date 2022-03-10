from typing import List


class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.

        === Solution ===
        To rotate the matrix by 90 degrees clockwise, we can reverse the rows of the matrix and then transpose the indices.
        To rotate the matrix by 90 degrees counter-clockwise, we can transpose the indices and then reverse the rows
        """

        i, j = 0, len(matrix) - 1

        while i < j:
            matrix[i], matrix[j] = matrix[j], matrix[i]
            i += 1
            j -= 1
 
        for i in range(len(matrix)):
            for j in range(i + 1, len(matrix[i])):
                matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]


