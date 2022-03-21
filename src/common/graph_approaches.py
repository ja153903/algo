from typing import List
from collections import defaultdict, deque


"""
Union Find with Rank

Use Cases
---------
* Finding number of connected components
* Finding largest or smallest connected components
"""

class UnionFind:
    def __init__(self, n: int) -> None:
        self.n = n
        self.parent = [i for i in range(n)]
        self.rank = [0] * n

    def find(self, u: int) -> int:
        if self.parent[u] != u:
            self.parent[u] = self.find(self.parent[u])

        return self.parent[u]

    def union(self, u: int, v: int) -> None:
        pu, pv = self.find(u), self.find(v)

        if pu != pv:
            if self.rank[pu] < self.rank[pv]:
                self.parent[pu] = pv
                self.rank[pv] += 1
            else:
                self.parent[pv] = pu
                self.rank[pu] += 1


"""
Topological Sort via Khan's algorithm

We use this for DAGs

This variation we're using right now is a way to figure out
whether there exists a cycle in this graph.

If n == 0, this means that there is no cycle in our DAG.
"""

def khans_algorithm(n: int, edges: List[List[int]]) -> bool:
    # build graph
    graph = defaultdict(list)
    indegree = [0] * n

    for u, v in edges:
        graph[v].append(u)
        indegree[u] += 1

    queue = deque()
    for i, val in enumerate(indegree):
        if val == 0:
            queue.append(i)

    # we start our iteration from points where indegree was 0
    while queue:
        current = queue.popleft()
        n -= 1

        for next_node in graph[current]:
            indegree[next_node] -= 1

            if indegree[next_node] == 0:
                queue.append(next_node)

    return n == 0

