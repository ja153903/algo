from typing import List


class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        result = []

        rows, cols = len(matrix), len(matrix[0])

        col_start, col_end = 0, cols - 1
        row_start, row_end = 0, rows - 1

        while col_start <= col_end and row_start <= row_end:
            for i in range(col_start, col_end + 1):
                result.append(matrix[row_start][i])

            row_start += 1

            for i in range(row_start, row_end + 1):
                result.append(matrix[i][col_end])

            col_end -= 1

            if row_start <= row_end:
                for i in range(col_end, col_start - 1, -1):
                    result.append(matrix[row_end][i])

                row_end -= 1

            if col_start <= col_end:
                for i in range(row_end, row_start - 1, -1):
                    result.append(matrix[i][col_start])

                col_start += 1

        return result
