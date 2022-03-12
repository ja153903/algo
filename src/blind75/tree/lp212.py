from typing import List
from collections import defaultdict


class TrieNode:
    def __init__(self):
        self.has_word = False
        self.children = defaultdict(TrieNode)


class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word: str) -> None:
        node = self.root

        for ch in word:
            node = node.children[ch]

        node.has_word = True

    def search(self, word: str) -> bool:
        node = self.root

        for ch in word:
            if ch not in node.children:
                return False

            node = node.children[ch]

        return node.has_word


"""
This problem requires us to use a Trie
as well as some typical DFS to go through all the positions
"""
class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        result = []
        trie = Trie()
        node = trie.root

        for word in words:
            trie.insert(word)

        for i in range(len(board)):
            for j in range(len(board[0])):
                self.dfs(board, node, i, j, "", result)

        return result

    def dfs(self, board: List[List[str]], node: TrieNode, i: int, j: int, current: str, result: List[str]) -> None:
        if node.has_word:
            result.append(current)
            # setting has word to false allows us to make sure that we don't add the same word to the result array
            node.has_word = False

        if i < 0 or j < 0 or i >= len(board) or j >= len(board[0]):
            return

        tmp = board[i][j]
        child = node.children.get(tmp)
        if not child:
            return

        board[i][j] = "$"

        self.dfs(board, child, i + 1, j, current + tmp, result)
        self.dfs(board, child, i - 1, j, current + tmp, result)
        self.dfs(board, child, i, j + 1, current + tmp, result)
        self.dfs(board, child, i, j - 1, current + tmp, result)

        board[i][j] = tmp
