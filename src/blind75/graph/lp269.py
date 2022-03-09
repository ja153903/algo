"""
There is a new alien language that uses the English alphabet.
However, the order among the letters is unknown to you.

You are given a list of strings words from the alien language's
dictionary, where the strings in words are sorted lexicographically
by the rules of this new language.

Return a string of the unique letters in the new alien language 
sorted in lexicographically increasing order by the new language's rules.
If there is no solution, return "'. If there are multiple solutions,
return any of them.

=== Solution ===
This problem is looking for some sort of topological sort

TODO: Didn't finish this problem
"""
from typing import List


class Solution:
    def alienOrder(self, words: List[str]) -> str:
        adj = [[False for _ in range(26)] for _ in range(26)]
        visited = [0] * 26

        self.build_graph(words, adj, visited)

        sb = []

        for i in range(26):
            if visited[i] == 0:
                if not self.dfs(adj, visited, sb, i):
                    return ""

        return "".join(sb[::-1])

    def dfs(
        self, adj: List[List[bool]], visited: List[int], sb: List[str], i: int
    ) -> bool:
        visited[i] = 1  # 1 = currently visiting
        for j in range(26):
            if adj[i][j]:
                if visited[j] == 1:
                    return False
                if visited[j] == 0:
                    if not self.dfs(adj, visited, sb, j):
                        return False
        visited[i] = 2  # 2 = visited
        sb.append(chr(i + 97))

        return True

    def build_graph(
        self, words: List[str], adj: List[List[bool]], visited: List[int]
    ) -> None:
        visited = [-1 for _ in visited]

        for i in range(len(words)):
            for ch in words[i]:
                visited[ord(ch) - 97] = 0

            if i > 0:
                w1, w2 = words[i - 1], words[i - 2]
                length = min(len(w1), len(w2))
                for j in range(length):
                    c1, c2 = w1[j], w2[j]
                    if c1 != c2:
                        adj[ord(c1) - 97][ord(c2) - 97] = True
                        break
