from typing import List


class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        if not board:
            return False

        rows, cols = len((board)), len(board[0])

        for i in range(rows):
            for j in range(cols):
                if board[i][j] == word[0]:
                    if self.can_exist(board, word, i, j, 1):
                        return True

        return False

    def can_exist(
        self,
        board: List[List[str]],
        word: str,
        i: int,
        j: int,
        curr: int,
    ) -> bool:
        if curr == len(word):
            return True

        result = False
        temp = board[i][j]
        board[i][j] = " "
        for dr, dc in [[1, 0], [-1, 0], [0, 1], [0, -1]]:
            nr, nc = i + dr, j + dc

            if (
                nr < 0
                or nc < 0
                or nr >= len(board)
                or nc >= len(board[0])
                or board[nr][nc] != word[curr]
            ):
                continue

            result = result or self.can_exist(board, word, nr, nc, curr + 1)

        board[i][j] = temp

        return result
