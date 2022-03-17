from typing import List


class Solution:
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
        result = []

        self.dfs(graph, 0, result, [0])

        return result

    def dfs(
        self,
        graph: List[List[int]],
        node: int,
        result: List[List[int]],
        current: List[int],
    ) -> None:
        if node == len(graph) - 1:
            result.append(list(current))
            return

        for child in graph[node]:
            self.dfs(graph, child, result, current + [child])
