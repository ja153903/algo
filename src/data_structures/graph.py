"""
Union Find with Rank

Rank is preferred instead of height because if path compression technique
is used, then rank is not always equal to height. Also, size of trees
can also be used as rank. Using size as rank also yields worst case O(lg n)
"""


class UnionFind:
    def __init__(self, n: int):
        self.n = n
        self.parent = [i for i in range(n)]
        self.rank = [0] * n

    def find(self, node: int):
        if self.parent[node] != node:
            self.parent[node] = self.find(self.parent[node])

        return self.parent[node]

    def union(self, i: int, j: int):
        pi, pj = self.find(i), self.find(j)

        if pi != pj:
            if self.rank[pi] >= self.rank[pj]:
                self.parent[pj] = pi
                self.rank[pi] += 1
            else:
                self.parent[pi] = pj
                self.rank[pj] += 1

