from typing import DefaultDict, List, Set
from collections import defaultdict


class Solution:
    def validPath(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
        """
        This problem is a DFS. We should build the graph first. 
        """
        graph = defaultdict(set)
        visited = set()

        for u, v in edges:
            graph[u].add(v)
            graph[v].add(u)
        
        return self.dfs(graph, visited, source, destination)
    
    def dfs(self, graph: DefaultDict[int, Set[int]], visited: Set[int], source: int, destination: int) -> bool:
        if source == destination:
            return True

        if source in visited:
            return False
        
        visited.add(source)
        
        for child in graph.get(source, []):
            if child in visited:
                continue
            
            if self.dfs(graph, visited, child, destination):
                return True
        
        return False