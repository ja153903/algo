from typing import List


class Solution:
    def linear_space(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        rows, cols = set(), set()

        for i in range(len(matrix)):
            for j in range(len(matrix[i])):
                if matrix[i][j] == 0:
                    rows.add(i)
                    cols.add(j)

        for row in rows:
            for i in range(len(matrix[row])):
                matrix[row][i] = 0

        for col in cols:
            for i in range(len(matrix)):
                matrix[i][col] = 0

    def setZeroes(self, matrix: List[List[int]]) -> None:
        rows, cols = len(matrix), len(matrix[0])
        zero_row, zero_col = False, False

        for i in range(rows):
            for j in range(cols):
                if matrix[i][j] == 0:
                    if i == 0:
                        zero_row = True
                    if j == 0:
                        zero_col = True

                    matrix[0][j] = 0
                    matrix[i][0] = 0

        for i in range(1, rows):
            for j in range(1, cols):
                if matrix[i][0] == 0 or matrix[0][j] == 0:
                    matrix[i][j] = 0

        # if the first row should be all 0s
        if zero_row:
            for i in range(cols):
                matrix[0][i] = 0

        # if the first col should be all 0s
        if zero_col:
            for i in range(rows):
                matrix[i][0] = 0
