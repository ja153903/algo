from typing import List, DefaultDict
from collections import deque


def bfs(graph: DefaultDict[int, List[int]], start: int):
    visited = set()
    queue = deque()

    queue.append(start)
    visited.add(start)

    while queue:
        front = queue.popleft()

        print(f"Node: {front}")

        for child in graph.get(front, []):
            if child in visited:
                continue

            queue.append(child)
