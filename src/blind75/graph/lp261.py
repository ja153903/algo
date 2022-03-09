"""
Return if edges make up a valid tree.

We know that a tree is a graph with no cycle.
Return true if tree doesn't contain a cycle.

We can use union find here.

If undirected graph, use union find to detect cycle
if directed graph, use khan's algorithm
"""
from typing import List


class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        parent = [-1] * n

        for u, v in edges:
            pu = self.find(parent, u)
            pv = self.find(parent, v)

            # Given that this is undirected, we can create cycle here
            if pu == pv:
                return False

            parent[pu] = pv

        return len(edges) == n - 1

    def find(self, parent: List[int], node: int) -> int:
        if parent[node] == -1:
            return node

        if parent[node] != -1:
            parent[node] = self.find(parent, parent[node])

        return parent[node]
