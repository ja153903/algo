from typing import List


class Solution:
    def countBattleships(self, board: List[List[str]]) -> int:
        battleships = 0

        for i in range(len(board)):
            for j in range(len(board[i])):
                if board[i][j] == "X":
                    battleships += 1

                    self.dfs(board, i, j)
        return battleships

    def dfs(self, board: List[List[int]], i: int, j: int) -> None:
        if (
            i < 0
            or j < 0
            or i >= len(board)
            or j >= len(board[0])
            or board[i][j] == "."
        ):
            return

        board[i][j] = "."

        self.dfs(board, i + 1, j)
        self.dfs(board, i - 1, j)
        self.dfs(board, i, j + 1)
        self.dfs(board, i, j - 1)

    def clever_optimal(self, board: List[List[str]]) -> int:
        battleships = 0

        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j] == ".":
                    continue

                if i > 0 and board[i - 1][j] == "X":
                    continue

                if j > 0 and board[i][j - 1] == "X":
                    continue

                battleships += 1

        return battleships
