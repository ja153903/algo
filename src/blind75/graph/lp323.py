"""
Return the number of connected components in the graph

We can do this via union find
"""
from typing import List


class UnionFind:
    def __init__(self, n: int):
        self.parent = [i for i in range(n)]
        self.ranks = [0] * n
        self.n = n

    def find(self, n: int) -> int:
        if self.parent[n] != n:
            self.parent[n] = self.find(self.parent[n])

        return self.parent[n]

    def union(self, u: int, v: int) -> None:
        nu, nv = self.find(u), self.find(v)
        if nu != nv:
            if self.ranks[nu] >= self.ranks[nv]:
                self.parent[nv] = nu
                self.ranks[nu] += 1
            else:
                self.parent[nu] = nv
                self.ranks[nv] += 1


class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        uf = UnionFind(n)

        for u, v in edges:
            uf.union(u, v)

        return len(set([uf.find(i) for i in range(n)]))
